from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=32)


class Distance(models.Model):
    city_1 = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='distance_1')
    city_2 = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='distance_2')

    distance = models.FloatField()
