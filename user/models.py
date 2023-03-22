from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile_number = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self) -> str:
        return self.first_name

    def __str__(self):
        return self.username