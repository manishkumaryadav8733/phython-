from django.db import models

# Create your models here.
class Student(models.model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age = models.IntegerField()


