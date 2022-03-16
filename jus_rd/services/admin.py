from django.contrib import admin

from services.models import Service, ServiceType
# Register your models here.

admin.site.register(Service)
admin.site.register(ServiceType)