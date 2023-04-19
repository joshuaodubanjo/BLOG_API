from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from .models import *

# Create your serializers here

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'mobile_number', 'created_date', 'updated_date', 'user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'publish']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'publish']


class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Author
        fields = ['user', 'first_name', 'last_name', 'created_date', 'updated_date', 'author_post']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'posted_date', 'updated_date', 'slug', 'content', 'author', 'published', 'category', 'tag']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'comment', 'posted_at', 'disapproved', 'author']