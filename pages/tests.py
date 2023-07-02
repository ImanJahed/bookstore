from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView
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
        
        
        
class AboutPageTest(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse('about')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'pages/about.html')
        self.assertContains(self.response, 'About Page')
        self.assertNotContains(self.response, 'Hi, I should not be their')

    def test_url_resolve_about_page_view(self):
        view = resolve('/about')
        self.assertEqual(view.func.__name__ , AboutPageView.as_view().__name__)

    