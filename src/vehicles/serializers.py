from rest_framework import serializers

from vehicles.models import Trip, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'current_location', 'fuel_consumption', 'distance_traveled', 'fuel_consumed')
        read_only_fields = ('distance_traveled', 'fuel_consumed')

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('pk', 'vehicle', 'origin', 'destiny', 'distance_traveled', 'created')
        read_only_fields = ('distance_traveled', 'created')

    def validate(self, attrs):
        if attrs['origin'] != attrs['vehicle'].current_location:
            raise serializers.ValidationError('Vehicle current location is different from trip origin')
        return attrs

