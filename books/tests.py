from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from datetime import datetime
from .models import Book, Comment
# Create your tests here.
class BookTest(TestCase):
 
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='commentuser', email='commentuser@email.com', password='userpass')
        cls.book = Book.objects.create(title='Harry Potter', author=get_user_model().objects.create(username='JK Rowling'), price='35.00', published_date=datetime.now())
        cls.comment = Comment.objects.create(book=cls.book, author=cls.user, comment='Fascinating')
        cls.permission = Permission.objects.get(codename='Special_status')
        
    def test_ListView(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '35.00')
        
        
    def test_book_list_view_for_logged_in_user(self):
        self.client.login(username='commentuser', password='userpass')
        response = self.client.get('/books/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'Books List')
        self.assertContains(response, 'Harry Potter')
    

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book-list'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" %(reverse('account_login')))
        
        response = self.client.get(f"{reverse('account_login')}?next=/books/")
        self.assertContains(response, 'Log In')


    def test_detail_view(self):
        self.client.login(username='commentuser', password="userpass")
        self.user.user_permissions.add(self.permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, f'{self.book.title}')
        self.assertContains(response, 'Fascinating')