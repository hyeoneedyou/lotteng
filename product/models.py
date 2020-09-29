from django.db import models

class Product(models.Model):
    name = models.CharField(primary_key = True, max_length=45)
    info = models.TextField(null = True, blank=True) # markdown field로 변경예정
    price = models.IntegerField(null = True, blank=True)

    