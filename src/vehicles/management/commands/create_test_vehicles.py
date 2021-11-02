from random import choice, randint

from django.core.management.base import BaseCommand

from cities.models import City
from vehicles.models import Vehicle

class Command(BaseCommand):
    help = 'Create Random Vehicles'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        if City.objects.count() == 0:
            print('There are no cities to assign vehicles location')
            return None

        city_list = list(City.objects.all())

        vehicles = []
        quantity = options.get('quantity')
        for i in range(quantity):
            vehicles.append(Vehicle(
                id='VEH' + str(i+1).zfill(3),
                current_location=choice(city_list),
                fuel_consumption=randint(12,25)
            ))
        Vehicle.objects.bulk_create(vehicles)


