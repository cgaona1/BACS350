from django.test import TestCase, SimpleTestCase
from django.urls import reverse
#from .models import Hero
from .hero import *

# Create your tests here.
class CrudTest(TestCase):
    def test_num_heroes(self):
        num_heroes = len(list_heroes())
        self.assertEqual(num_heroes, 0)

    def test_hero_model(self):
        self.assertTrue

    def test_create_hero(self):
        add_hero(name = 'Bob', description = 'Im bob')
        num_heroes = len(list_heroes())
        self.assertEqual(num_heroes, 1)

    def test_read_hero(self):
        add_hero(name='Bob', description='Im bob')
        name = get_hero_name(1)
        description = get_hero_description(1)
        self.assertEqual(name,'Bob')
        self.assertEqual(description, 'Im bob')

    def test_update_hero(self):
        add_hero(name='Bob', description='Im bob')
        set_hero_name(1,'Peter')
        self.assertEqual(get_hero_name(1), 'Peter')

    def test_delete_hero(self):
        add_hero(name='Bob', description='Im bob')
        delete_hero(1)
        num_heroes = len(list_heroes())
        self.assertEqual(num_heroes, 0)


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/heroes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero_list.html')