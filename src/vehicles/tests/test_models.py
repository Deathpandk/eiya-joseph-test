from django.db import IntegrityError
from django.test import TestCase

from cities.models import City, Distance
from vehicles.models import Trip, Vehicle


class VehicleTestCase(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='Cdmx')
        self.vehicle_id = 'VEH001'
        self.vehicle = Vehicle.objects.create(
            id=self.vehicle_id,
            current_location=self.city,
            fuel_consumption=12
        )

    def test_vehicles_defaults(self):
        self.assertTrue(Vehicle.objects.exists())
        self.assertEqual(self.vehicle.distance_traveled, 0)
        self.assertEqual(self.vehicle.fuel_consumed, 0)

    def test_vehicle_duplicated_id(self):
        with self.assertRaises(IntegrityError):
            Vehicle.objects.create(
                id=self.vehicle_id, current_location=self.city, fuel_consumption=13
            )

class TripTestCase(TestCase):
    def setUp(self):
        self.city_1 = City.objects.create(name='Cdmx')
        self.city_2 = City.objects.create(name='Guadalajara')
        self.distance = 30
        self.distance_object = Distance.objects.create(
            city_1=self.city_1, city_2=self.city_2, distance=self.distance,
        )
        self.vehicle_id = 'VEH001'
        self.vehicle = Vehicle.objects.create(
            id=self.vehicle_id,
            current_location=self.city_1,
            fuel_consumption=12
        )

    def test_create_loop_trip(self):
        with self.assertRaises(IntegrityError):
            Trip.objects.create(
                vehicle=self.vehicle, origin=self.city_1, destiny=self.city_1
            )

    def test_create_trip(self):
        Trip.objects.create(
            vehicle=self.vehicle, origin=self.city_1, destiny=self.city_2
        )
        self.assertEqual(Trip.objects.count(), 1)

    def test_trip_distance_and_vehicle_variables(self):
        trip = Trip.objects.create(
            vehicle=self.vehicle, origin=self.city_1, destiny=self.city_2
        )
        self.assertEqual(trip.distance_traveled, self.distance)
        self.assertEqual(self.vehicle.distance_traveled, self.distance)
        self.assertEqual(self.vehicle.fuel_consumed, self.distance / self.vehicle.fuel_consumption)
        self.assertEqual(self.vehicle.current_location, self.city_2)

        Trip.objects.create(
            vehicle=self.vehicle, origin=self.city_2, destiny=self.city_1
        )
        self.assertEqual(self.vehicle.distance_traveled, self.distance * 2)
        self.assertEqual(self.vehicle.fuel_consumed, 2 * self.distance / self.vehicle.fuel_consumption)
        self.assertEqual(self.vehicle.current_location, self.city_1)
