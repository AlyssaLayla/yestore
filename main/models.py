from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, name="name")
    price = models.IntegerField(name="price")
    description = models.TextField(name="description")
