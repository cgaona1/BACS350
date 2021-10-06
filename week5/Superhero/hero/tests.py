from django.test import TestCase
from .models import Hero
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
        h = get_hero_name('Bob')
        self.assertEqual(h,'Bob')


