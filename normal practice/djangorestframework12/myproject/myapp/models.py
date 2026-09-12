from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    number = models.IntegerField()
    

# Create your models here.
