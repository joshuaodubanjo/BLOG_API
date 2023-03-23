from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile_number = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        return self.first_name

    def __str__(self):
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    birth_date = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile\'s'

    def full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.first_name
    