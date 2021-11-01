from django.urls import include, path

app_name = 'vehicles'
urlpatterns = [
    path('api/', include('vehicles.api.urls')),
]
