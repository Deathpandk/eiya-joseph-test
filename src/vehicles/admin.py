from django.contrib import admin
from .models import Trip, Vehicle

# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_location', 'fuel_consumption', 'distance_traveled', 'fuel_consumed')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'origin', 'destiny', 'distance_traveled')