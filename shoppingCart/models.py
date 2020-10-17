from customer.models import Customer
from onSaleProduct.models import OnSaleProduct
from django.db import models

class ShoppingCart(models.Model):
    onSaleProduct = models.ForeignKey(OnSaleProduct, models.SET_NULL, blank = True, null = True)
    customer = models.ForeignKey(Customer, models.SET_NULL, blank = True, null = True)
    count = models.IntegerField(null = True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

