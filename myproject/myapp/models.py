from django.db import models

# Create your models here.from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)              # Product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with 2 decimal places
    quantity = models.PositiveIntegerField(default=1)    # Quantity (only positive numbers)
    image = models.ImageField(upload_to='products/')     # Image upload folder: media/products/


    def __str__(self):
        return self.name
