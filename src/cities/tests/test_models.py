from datetime import date

from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse_lazy

from cities.models import City, Distance


class CityTestCase(TestCase):
    def setUp(self):
        self.name = 'Chicago'
        self.city = City.objects.create(name=self.name)

    def test_city_exists(self):
        employee = City.objects.filter(name=self.name)
        self.assertTrue(employee.exists())

    def test_city_duplicated_name(self):
        with self.assertRaises(IntegrityError):
            City.objects.create(name=self.name)

class DistanceTestCase(TestCase):
    def setUp(self):
        self.chicago = City.objects.create(name='Chicago')
        self.california = City.objects.create(name='California')
        self.texas = City.objects.create(name='Texas')

    def test_create(self):
        Distance.objects.create(city_1=self.california, city_2=self.chicago, distance=80)
        self.assertTrue(Distance.objects.exists())

    def test_creating_with_missing_city_1(self):
        with self.assertRaises(IntegrityError):
            Distance.objects.create(city_2=self.california, distance=20)

    def test_creating_with_missing_city_2(self):
        with self.assertRaises(IntegrityError):
            Distance.objects.create(city_1=self.california, distance=20)

    def test_creating_with_missing_distance(self):
        with self.assertRaises(IntegrityError):
            Distance.objects.create(city_2=self.california, city_1=self.texas)

    def test_create_duplicated_distance(self):
        with self.assertRaises(IntegrityError):
            Distance.objects.create(city_1=self.california, city_2=self.chicago, distance=80)
            Distance.objects.create(city_1=self.california, city_2=self.chicago, distance=80)

    def test_create_inverse_distance(self):
        with self.assertRaises(IntegrityError):
            Distance.objects.create(city_1=self.california, city_2=self.chicago, distance=80)
            Distance.objects.create(city_2=self.california, city_1=self.chicago, distance=80)
        self.assertEqual(1, Distance.objects.count())
