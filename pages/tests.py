from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView
# Create your tests here.
class HomePageTest(SimpleTestCase):
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'Home Page')
        self.assertNotContains(response, 'Hi, I should not be on page')
        
    def test_homepage_url_resolve_HomePageView(self):
        view = resolve('/')

        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)