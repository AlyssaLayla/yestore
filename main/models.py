from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, name="name")
    price = models.IntegerField(name="price")
    quantity = models.IntegerField(name="quantity")
    description = models.TextField(name="description")
    category = models.CharField(max_length=255, name="category")
