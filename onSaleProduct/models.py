from django.db import models
from product.models import Product
from shop.models import Shop
from shop.models import Shop

class OnSaleProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, blank = True, null = True)
    shop = models.ForeignKey(Shop, models.SET_NULL, blank = True, null = True)
    kinds = models.CharField(max_length=45)
    price = models.IntegerField(null = True, blank=True)
    stock = models.IntegerField(null = True, blank=True)
    endDate = models.DateTimeField(null = True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)