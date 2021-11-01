from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'api'
urlpatterns = [
    path('trips', views.CreateTrip.as_view(), name='trips'),
]

router = DefaultRouter(trailing_slash=False)
router.register('vehicles', views.VehicleViewSet, basename='vehicles')

urlpatterns += router.urls
