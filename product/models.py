from django.db import models

class Product(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('w', 'withdrawn')
    )

    name = models.CharField(primary_key = True, max_length=45)
    info = models.TextField(null = True, blank=True) # markdown field로 변경예정
    price = models.IntegerField(null = True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    