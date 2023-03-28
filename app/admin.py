from django.contrib import admin

from .models import Author, Comment, Category, Post, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish']
    list_display_links = ['id', 'title']
    list_editable = ['publish']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish']
    list_display_links = ['id', 'title']
    list_editable = ['publish']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user']
    list_display_links = ['id', 'full_name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'posted_date', 'published']
    list_display_links = ['id', 'title']
    list_editable = ['published',]
    list_filter = ['posted_date', 'updated_date']
    readonly_fields = ['posted_date', 'updated_date']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Connected Models', {
            'fields': ('author', 'category', 'tag')
        }),
        ('Post Details', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Important Date', {
            'fields': ('posted_date', 'updated_date')
        }),
        ('Publish', {
            'fields': ('published',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'post_comment', 'post_author', 'posted_at', 'disapproved']
    list_display_links = ['id', 'post_comment']
    list_editable = ['disapproved']