from django.db import models

# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    place = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    description = models.CharField(max_length=100)
    
