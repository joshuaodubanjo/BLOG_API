from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import F
from django.db.models.aggregates import Count

from .models import CustomUser, Profile
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
        "username",
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    list_editable = ['is_staff', 'is_active']
    list_display_links = ['username', 'email']
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
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name'),
            }),
   )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'full_name', 'email', 'mobile_number']
    list_display_links = ["id", "full_name"]
    list_filter = ('birth_date',)
    readonly_fields = ['created_date', 'updated_date']
    search_fields= ['first_name__istartswith', 'last_name__istartswith']
    
    # def full_name(self, obj:Profile):
    #     return f'{obj.first_name} {obj.last_name}'
    
    TEXT = 'When a user is created, the profile is is also created!'
    fieldsets = (
        ('User', {
            'fields': ('user',),
            'description': '%s' % TEXT,
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'birth_date')
        }),
        ('Contact Info', {
            'fields': ('email', 'mobile_number')
        }),
        ('Important Dates', {
            'fields': ('created_date', 'updated_date')
        }),
    )