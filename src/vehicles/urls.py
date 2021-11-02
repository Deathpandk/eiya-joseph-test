from django.urls import include, path

from . import views

app_name = 'vehicles'
urlpatterns = [
    path('api/', include('vehicles.api.urls')),
    path('', views.VehiclesIndex.as_view(), name='index'),
]
