from django.contrib import admin
from .models import OnSaleProduct

class OnSaleProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'shop', 'kinds', 'price', 'stock', 'endDate', 'createdAt', 'updatedAt']
    list_filter = ['product', 'kinds', 'shop__company']

admin.site.register(OnSaleProduct, OnSaleProductAdmin)