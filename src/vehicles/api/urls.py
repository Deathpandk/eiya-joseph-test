from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('trips', views.CreateTrip.as_view(), name='trips'),
]
