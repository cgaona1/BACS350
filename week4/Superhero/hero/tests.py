from django.http import response
from django.test import SimpleTestCase
from django.test import TestCase

'''
# Create your simple tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
'''
# Create your test here


class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_hero_page_status_code(self):
        response = self.client.get('/hero/')
        self.assertEqual(response.status_code, 200)
