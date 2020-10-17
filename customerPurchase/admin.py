from django.contrib import admin
from .models import CustomerPurchase


class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'onSaleProduct', 'customer', 'count', 'payment', 'createdAt', 'updatedAt']
    list_filter = ['customer', 'onSaleProduct']

admin.site.register(CustomerPurchase, CustomerPurchaseAdmin)
