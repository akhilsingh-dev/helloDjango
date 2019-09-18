from django.test import SimpleTestCase

# Create your tests here.
class PageTests(SimpleTestCase):
    def test_page_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_about_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
