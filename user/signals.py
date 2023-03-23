
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, Profile
# Create your signals here

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.save()
        print('Profile Created')

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print('Profile Updated')
