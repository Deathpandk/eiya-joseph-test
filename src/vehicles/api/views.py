from rest_framework.generics import CreateAPIView

from vehicles.models import Trip
from vehicles.serializers import TripSerializer

class CreateTrip(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
