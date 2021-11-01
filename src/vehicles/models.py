from django.db import IntegrityError, models

from cities.utils import get_distance

# Create your models here.

class Vehicle(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    current_location = models.ForeignKey('cities.City', on_delete=models.PROTECT)
    fuel_consumption = models.FloatField(help_text='km/lt')
    distance_traveled = models.FloatField(default=0)
    fuel_consumed = models.FloatField(default=0, help_text='lts')

    def update_variables(self):
        distance_traveled = self.trip_set.aggregate(
            models.Sum('distance_traveled')
        ).get('distance_traveled__sum', None)
        self.distance_traveled = distance_traveled if distance_traveled else 0
        self.fuel_consumed = self.distance_traveled / self.fuel_consumption
        self.current_location = self.trip_set.first().destiny
        self.save()

class Trip(models.Model):
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    origin = models.ForeignKey('cities.City', on_delete=models.PROTECT, related_name='trips_send')
    destiny = models.ForeignKey('cities.City', on_delete=models.PROTECT, related_name='trips_arrived')
    distance_traveled = models.FloatField(editable=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def get_distance_traveled(self):
        return get_distance(self.origin, self.destiny)

    def save(self, *args, **kwargs):
        if hasattr(self, 'origin') and hasattr(self, 'destiny') and (self.origin == self.destiny):
            raise IntegrityError
        self.distance_traveled = self.get_distance_traveled()
        super(Trip, self).save(*args, **kwargs)
        self.vehicle.update_variables()
