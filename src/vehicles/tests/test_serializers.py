from django.test import TestCase

from cities.models import City
from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer

class TestVehicleSerializer(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='Cdmx')
        self.vehicle = Vehicle.objects.create(
            id="VEH001", current_location=self.city, fuel_consumption=15,
        )

    def test_serializer_data(self):
        serializer = VehicleSerializer(instance=self.vehicle)
        keys = serializer.data.keys()
        self.assertTrue("id" in keys)
        self.assertTrue("current_location" in keys)
        self.assertTrue("fuel_consumption" in keys)
        self.assertTrue("distance_traveled" in keys)
        self.assertTrue("fuel_consumed" in keys)

    def test_serializer_creation_read_only_fields(self):
        data = {
            "id": "VEH002",
            "current_location": self.city.pk,
            "fuel_consumption": 10,
            "distance_traveled": 100,
            "fuel_consumed": 100,
        }
        serializer = VehicleSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        obj = Vehicle.objects.get(id="VEH002")
        self.assertEqual(obj.distance_traveled, 0)
        self.assertEqual(obj.fuel_consumed, 0)
