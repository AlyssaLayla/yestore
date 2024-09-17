from django.db import models
import uuid 

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, name="name")
    price = models.IntegerField(name="price")
    quantity = models.IntegerField(name="quantity", default=0)
    description = models.TextField(name="description")
    category = models.CharField(max_length=255, name="category", default="Uncategorized")

