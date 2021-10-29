from django.db import models

# Create your models here.

class Vehicle(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    current_location = models.ForeignKey('cities.City', on_delete=models.PROTECT)
    fuel_consumption = models.FloatField(help_text='km/lt')
    distance_traveled = models.FloatField(default=0)
    fuel_consumed = models.FloatField(default=0)

class Trip(models.Model):
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    origin = models.ForeignKey('cities.City', on_delete=models.PROTECT, related_name='trips_send')
    destiny = models.ForeignKey('cities.City', on_delete=models.PROTECT, related_name='trips_arrived')
    created = models.DateTimeField(auto_now_add=True)