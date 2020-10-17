from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phoneNumber = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    permission = models.IntegerField(null = True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user = instance)
    
@receiver(post_save, sender = User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()

