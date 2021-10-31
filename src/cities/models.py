from django.db import IntegrityError, models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Distance(models.Model):
    city_1 = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='distance_1')
    city_2 = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='distance_2')
    distance = models.FloatField()

    class Meta:
        unique_together = ('city_1', 'city_2')

    def save(self, *args, **kwargs):
        if hasattr(self, 'city_1') and hasattr(self, 'city_2') and Distance.objects.filter(
            city_1=self.city_2, city_2=self.city_1,
        ):
            raise IntegrityError
        super(Distance, self).save(*args, **kwargs)

