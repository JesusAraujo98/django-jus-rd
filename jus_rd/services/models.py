from django.db import models

# Create your models here.
class ServiceType(models.Model):
    type_name = models.CharField(max_length=100)
    type_image = models.ImageField()
    type_description = models.TextField(max_length=200)

class Service(models.Model):
    service = models.TextField(max_length=100)
    service_description = models.TextField(max_length=  200)
    service_price = models.FloatField(blank=True)
    is_static = models.BooleanField(default= True)
    documents=models.FileField(blank=True)
    has_documents = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    