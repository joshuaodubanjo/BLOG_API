from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, unique=True)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField(help_text='The age will be populated after you save your date of birth_date. It can\'t be edited', null=True)
    mobile_number = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile\'s'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # @property
    # def age(birth_date):
    #     import datetime
    #     today = date.today()
    #     age = today.year - birth_date.year - ((today.month, today.day) > (birth_date.month, birth_date.day))
    #     return age

    def __str__(self):
        return self.first_name
    