from django.db import models

class Company(models.Model):
    name = models.CharField(pk = True, max_length=45)
    info = models.TextField() # markdown field로 변경예정
    price = models.IntegerField()

    