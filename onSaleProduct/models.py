from django.db import models
from product.models import Product
from shop.models import Shop

class OnSaleProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, blank = True, null = True)
    kinds = models.CharField(pk = True, max_length=45)
    price = models.IntegerField()
    stock = models.IntegerField()
    endDate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)