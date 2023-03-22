from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Create your forms here 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class CustomUserChangeform(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = UserChangeForm.Meta.fields