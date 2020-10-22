from django.contrib import admin
from .models import Shop, AuthNumber

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'longitude', 'latitude', 'company']
    list_filter = ['company']

class AuthNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'auth_number']
    list_filter = ['shop']

admin.site.register(Shop, ShopAdmin)
admin.site.register(AuthNumber, AuthNumberAdmin)