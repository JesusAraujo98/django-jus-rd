from re import M
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    
