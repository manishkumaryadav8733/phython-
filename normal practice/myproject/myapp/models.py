from django.db import models

# Create your models here.
class categeory(models.Model):
    categeory =models.CharField(max_length=20)

class product(models.Model):
    Categeory =models.ForeignKey(categeory,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image")