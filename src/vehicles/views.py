from django.views.generic import TemplateView


class VehiclesIndex(TemplateView):
    template_name = 'vehicles/index.html'