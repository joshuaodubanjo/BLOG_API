from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

from . import views 
# from .views import *

# Create your urls here

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet, basename='profiles')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('posts', views.PostViewSet, basename='posts')
router.register('authors', views.AuthorViewSet, basename='authors')
router.register('tags', views.TagViewSet, basename='tags')

post_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
post_router.register('comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(post_router.urls)),
]


# urlpatterns += router.urls