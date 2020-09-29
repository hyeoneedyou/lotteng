from django.db import models

class Company(models.Model):
    name = models.CharField(pk = True, max_length=45)
    