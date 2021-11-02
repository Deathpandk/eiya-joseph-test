from django.core.management.base import BaseCommand

from cities.models import City, Distance

class Command(BaseCommand):
    help = 'Create A B C Cities'

    def handle(self, *args, **options):
        if City.objects.all():
            return None
        A = City.objects.create(name='Ciudad A')
        B = City.objects.create(name='Ciudad B')
        C = City.objects.create(name='Ciudad C')

        distances = [
            Distance(city_1=A, city_2=A, distance=0),
            Distance(city_1=B, city_2=B, distance=0),
            Distance(city_1=C, city_2=C, distance=0),
            Distance(city_1=A, city_2=B, distance=1),
            Distance(city_1=A, city_2=C, distance=2),
            Distance(city_1=B, city_2=C, distance=4),
        ]
        Distance.objects.bulk_create(distances)
