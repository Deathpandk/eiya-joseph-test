from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from vehicles.models import Trip, Vehicle
from vehicles.serializers import TripSerializer, VehicleSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class CreateTrip(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
