from django.contrib.auth import get_user, get_user_model
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


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'


    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)