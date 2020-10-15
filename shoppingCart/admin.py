from django.contrib import admin
from .models import ShoppingCart

class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'onSaleProduct', 'customer', 'count', 'createdAt', 'updatedAt']
    list_filter = ['customer', 'onSaleProduct']

admin.site.register(ShoppingCart, ShoppingCartAdmin)
