from django.shortcuts import render
from .models import ServiceType, Service
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'services/index.html'
    context_object_name = "service_type_list"

    def get_queryset(self):
        return ServiceType.objects.all()

