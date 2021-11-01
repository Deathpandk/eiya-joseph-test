from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cities.models import City, Distance
from vehicles.models import Trip, Vehicle


class VehicleAPITest(APITestCase):
    def setUp(self):
        self.api_url = '/api/vehicles'
        self.city_1 = City.objects.create(name='Cdmx')
        self.city_2 = City.objects.create(name='Guadalajara')
        Distance.objects.create(
            city_1=self.city_1, city_2=self.city_2, distance=15
        )
        self.vehicle = Vehicle.objects.create(
            id='VEH001', current_location=self.city_1, fuel_consumption=13
        )

    def test_get_objects(self):
        response = self.client.get(self.api_url)
        self.assertEqual(len(response.data), Vehicle.objects.count())

    def test_create_object(self):
        response = self.client.post(
            self.api_url,
            data={
                'id': 'VEH002',
                'current_location': self.city_2.pk,
                'fuel_consumption': 15,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Vehicle.objects.filter(id='VEH002').exists())

    def test_update_object(self):
        response = self.client.patch(
            self.api_url + '/' + self.vehicle.pk,
            data={
                'fuel_consumption': 17,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vehicle = Vehicle.objects.get(id='VEH001')
        self.assertTrue(vehicle.fuel_consumption, 17)

    def test_delete_object(self):
        response = self.client.delete(
            self.api_url + '/' + self.vehicle.pk
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vehicle.objects.count(), 0)


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
