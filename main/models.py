from django.db import models

# Create your models here.
from django.db import models

#name = CharField
#price = IntegerField
#description = TextField

class Product(models.Model):
    name = models.CharField(max_length=255, name="name")
    price = models.IntegerField(name="price")
    description = models.TextField(name="description")
