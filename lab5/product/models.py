from django.db import models
from decimal import Decimal
from django.forms import ModelForm

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32, blank=False)
    description = models.TextField(max_length=142, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=4,default=Decimal('00.00'), blank=False)

    def __str__(self):
        return self.name + ' ' + self.description + ' ' + str(self.price)
