from django.contrib import admin
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'longitude', 'latitude', 'company']

admin.site.register(Shop)