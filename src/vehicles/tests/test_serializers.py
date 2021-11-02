from django.test import TestCase

from cities.models import City, Distance
from cities.utils import get_distance
from vehicles.models import Trip, Vehicle
from vehicles.serializers import TripSerializer, VehicleSerializer


class TestVehicleSerializer(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='Cdmx')
        self.vehicle = Vehicle.objects.create(
            id='VEH001', current_location=self.city, fuel_consumption=15,
        )

    def test_serializer_data(self):
        serializer = VehicleSerializer(instance=self.vehicle)
        keys = serializer.data.keys()
        self.assertTrue('id' in keys)
        self.assertTrue('current_location' in keys)
        self.assertTrue('current_location_name' in keys)
        self.assertTrue('fuel_consumption' in keys)
        self.assertTrue('distance_traveled' in keys)
        self.assertTrue('fuel_consumed' in keys)

    def test_serializer_creation_read_only_fields(self):
        data = {
            'id': 'VEH002',
            'current_location': self.city.pk,
            'fuel_consumption': 10,
            'distance_traveled': 100,
            'fuel_consumed': 100,
        }
        serializer = VehicleSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        obj = Vehicle.objects.get(id='VEH002')
        self.assertEqual(obj.distance_traveled, 0)
        self.assertEqual(obj.fuel_consumed, 0)

class TestTripSerializer(TestCase):
    def setUp(self):
        self.city_1 = City.objects.create(name='Cdmx')
        self.city_2 = City.objects.create(name='Guadalajara')
        Distance.objects.create(city_1=self.city_1, city_2=self.city_2, distance=20)
        self.vehicle = Vehicle.objects.create(
            id='VEH001', current_location=self.city_1, fuel_consumption=15,
        )

    def test_serializer_data(self):
        trip = Trip.objects.create(
            vehicle=self.vehicle, origin=self.city_1, destiny=self.city_2
        )
        serializer = TripSerializer(instance=trip)
        keys = serializer.data.keys()
        self.assertTrue('pk' in keys)
        self.assertTrue('vehicle' in keys)
        self.assertTrue('origin' in keys)
        self.assertTrue('destiny' in keys)
        self.assertTrue('distance_traveled' in keys)
        self.assertTrue('created' in keys)

    def test_vehicle_not_in_trip_origin(self):
        data = {
            'vehicle': self.vehicle.id,
            'origin': self.city_2.pk,
            'destiny': self.city_1.pk,
        }
        serializer = TripSerializer(data=data)
        serializer.is_valid()

        self.assertFalse(serializer.is_valid())

    def test_trip_creation(self):
        data = {
            'vehicle': self.vehicle.id,
            'origin': self.city_1.pk,
            'destiny': self.city_2.pk,
        }
        serializer = TripSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        trip = Trip.objects.get(pk=serializer.data.get('pk'))

        self.assertEqual(trip.origin, self.city_1)
        self.assertEqual(trip.destiny, self.city_2)
        self.assertEqual(trip.distance_traveled, get_distance(self.city_1, self.city_2))
        self.assertEqual(trip.vehicle, self.vehicle)
