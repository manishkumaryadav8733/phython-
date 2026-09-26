from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("MANAGER", "Inventory Manager"),
        ("STAFF", "Warehouse Staff"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="STAFF"
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username