from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'phoneNumber', 'email', 'permission']
    list_filter = ['permission']
    list_display_links = ['id', 'email', 'user']

admin.site.register(Customer, CustomerAdmin)
