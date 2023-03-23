
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models
from .models import CustomUser, Profile

# Create your signals here

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name = instance.first_name, last_name = instance.last_name, email=instance.email, mobile_number=instance.mobile_number)
        instance.profile.save()
        print('Profile Created')