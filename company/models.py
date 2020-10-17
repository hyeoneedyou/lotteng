from django.db import models

class Company(models.Model):
    name = models.CharField(primary_key = True, max_length=45)
    
    def __str__(self):
        return self.name