
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve



# Create your tests here.
class CustomUserTest(TestCase):
    def test_user_create(self):
        USER = get_user_model()
        user = USER.objects.create_user(
            username="testuser", email="testuser@email.com", password="testuserpass"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        USER = get_user_model()
        test_superuser = USER.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@email.com",
            password="testsuper123",
        )

        self.assertEqual(test_superuser.username, "testsuperuser")
        self.assertEqual(test_superuser.email, "testsuperuser@email.com")
        self.assertTrue(test_superuser.is_active)
        self.assertTrue(test_superuser.is_staff)
        self.assertTrue(test_superuser.is_superuser)



class SignUpTest(TestCase):
    username = 'newuser'
    email = 'newuser@emai.com'
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        
    
    def test_signup_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there, I should not be their')


    def test_signup_view_create_new_user(self):
        new_user = get_user_model().objects.create_user(username=self.username, email=self.email)
    
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
