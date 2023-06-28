from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class AccountTest(TestCase):
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
