from django.contrib import admin
from .models import OnSaleProduct

class OnSaleProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'kinds', 'price', 'stock', 'endDate', 'createdAt', 'updatedAt']
    list_filter = ['product', 'kinds']

admin.site.register(OnSaleProduct, OnSaleProductAdmin)