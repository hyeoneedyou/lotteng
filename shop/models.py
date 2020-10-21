from django.db import models
from company.models import Company

class Shop(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45)
    company = models.ForeignKey(Company, models.SET_NULL, blank = True, null = True)


    def __str__(self):
        return "["+self.name+"]"+self.company.name