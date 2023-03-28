from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *
from user.models import *

# Create your signals here
@receiver(post_save, sender=CustomUser)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance, first_name = instance.first_name, last_name = instance.last_name)
        instance.author.save()
        print('Author Created')