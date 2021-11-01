from rest_framework import serializers

from vehicles.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("id", "current_location", "fuel_consumption", "distance_traveled", "fuel_consumed")
        read_only_fields = ("distance_traveled", "fuel_consumed")
