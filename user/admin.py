from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeform

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeform
    model = CustomUser
    # fields = list(BaseUserAdmin.fieldsets)
    # fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'username')})
    # BaseUserAdmin.fieldsets = tuple(fields)


    list_display = [
        "first_name",
        "email",
        "username",
        "is_staff",
        "is_active",
    ]
    # search_fields = ['email']
    fieldsets = (
        ('Custom User', {'fields': ('username', 'password'),}),
        ('Contact_Info', {'fields': ('email', 'mobile_number'),}),
        ('Personal Info', {'fields': ('first_name', 'last_name'),}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),}),
        ('Important dates', {'fields': ('last_login', 'date_joined'),}),
        # ('Contact info', {'fields': ('contact_no',),}),
    )
    add_fieldsets = (
        ('Create Custom User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name'),
            }),
   )