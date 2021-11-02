from django.contrib import admin
from .models import City, Distance

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('city_1', 'city_2', 'distance')