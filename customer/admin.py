from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'phoneNumber', 'email', 'permission']

admin.site.register(Customer, CustomerAdmin)
