from django.db import models
from mdeditor.fields import MDTextField

class Product(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('w', 'withdrawn')
    )

    name = models.CharField(primary_key = True, max_length=45)
    info = MDTextField(null = True, blank=True)
    represent_image = models.ImageField(blank = True, upload_to = "product/")
    sub_name = models.TextField(null = True, blank=True)
    price = models.IntegerField(null = True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    
    def __str__(self):
        return self.name