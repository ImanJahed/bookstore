from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime
from .models import Book
from accounts.models import CustomUserModel
# Create your tests here.
class BookTest(TestCase):
    # new_user = get_user_model().objects.create(username='JK Rowling1', email='rowling@email', password='testpassword')
    
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title='Harry Potter', author=get_user_model().objects.create(username='JK Rowling'), price='35.00', published_date=datetime.now())
    
    def test_list_view(self):
        response = self.client.get('/books/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'Books List')

    
    def test_ListView(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '35.00')


    def test_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, f'{self.book.title}')