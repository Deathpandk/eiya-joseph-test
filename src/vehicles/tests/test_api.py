from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cities.models import City, Distance
from vehicles.models import Trip, Vehicle

class TripAPITest(APITestCase):
    def setUp(self):
        self.city_1 = City.objects.create(name='Cdmx')
        self.city_2 = City.objects.create(name='Guadalajara')
        Distance.objects.create(
            city_1=self.city_1, city_2=self.city_2, distance=15
        )
        self.vehicle = Vehicle.objects.create(
            id='VEH001', current_location=self.city_1, fuel_consumption=13
        )

    def test_create_trip_api(self):
        response = self.client.post(
            reverse('vehicles:api:trips'),
            data={
                'vehicle': self.vehicle.id,
                'origin': self.city_1.pk,
                'destiny': self.city_2.pk,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trip.objects.count(), 1)
