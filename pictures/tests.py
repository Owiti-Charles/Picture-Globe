from django.test import TestCase

from .models import Image, Category, Location


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

        self.image_test = Image(id=1, name= 'image', description='this is a test image', location=self.location)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))
