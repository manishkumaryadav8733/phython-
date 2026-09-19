from django.db import models

# Create your models here.
class Categeory(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    categeory = models.ForeignKey(Categeory,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="products")