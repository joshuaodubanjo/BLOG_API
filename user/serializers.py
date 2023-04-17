from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import Userserializer, BaseuserSerializer

from .models import CustomUser

# Create your serializers here

# To add more fields in registration
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


# This is to overwrite the current user
class UserSerializer(BaseuserSerializer):
    class Meta(BaseuserSerializer):
        fields = ['id', 'username', 'email', 'first_namer', 'last_name'] 



class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'birth_date', 'mobile_number', 'created_date', 'updated_date', 'user']


