from django.views.generic import TemplateView

from cities.models import City

class VehiclesIndex(TemplateView):
    template_name = 'vehicles/index.html'
    extra_context = {'cities': City.objects.all()}
