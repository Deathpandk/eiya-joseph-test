from django.test import TestCase

from cities.models import City, Distance
from cities.utils import get_distance

class DistanceTestCase(TestCase):
    def setUp(self):
        self.chicago = City.objects.create(name='Chicago')
        self.california = City.objects.create(name='California')
        self.texas = City.objects.create(name='Texas')
        Distance.objects.create(city_1=self.california, city_2=self.chicago, distance=80)
        Distance.objects.create(city_1=self.chicago, city_2=self.chicago, distance=0)

    def test_get_distances(self):
        self.assertEqual(80, get_distance(self.california, self.chicago))
        self.assertEqual(80, get_distance(self.chicago, self.california))
        self.assertEqual(0, get_distance(self.chicago, self.chicago))
        self.assertEqual(None, get_distance(self.chicago, self.texas))
