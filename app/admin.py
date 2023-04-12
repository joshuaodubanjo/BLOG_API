from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet

from .models import Author, Comment, Category, Post, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish', 'post_count']
    list_display_links = ['id', 'title']
    list_editable = ['publish']
    search_fields = ['title__icontains']

    @admin.display(ordering='post_count')
    def post_count(self, Category):
        return Category.post_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            post_count = Count('post')
        )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish']
    list_display_links = ['id', 'title']
    list_editable = ['publish']
    search_fields = ['title__icontains']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user']
    list_display_links = ['id', 'full_name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['clear_published']
    autocomplete_fields = ['category', 'tag']
    list_display = ['id', 'title', 'author', 'category', 'posted_date', 'published', 'word_length']
    list_select_related = ['category']
    list_display_links = ['id', 'title']
    list_editable = ['published',]
    list_filter = ['category','posted_date', 'updated_date']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['posted_date', 'updated_date']
    search_fields = ['title__icontains']
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
    # @admin.display(ordering='title')
    def word_length(self, Post):
        counter = 0
        for count in Post.content:
            counter+=1
        return counter
        # if Post.content.len() < str(150):
        #     return 'Short Post'
        # return 'Long Post'

    @admin.action(description='clear_published')
    def clear_published(self, request, queryset: QuerySet):
        update_pub = queryset.update(published=False)
        self.message_user(request, f'{update_pub} products were successfully unpublished', messages.ERROR)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'post_comment', 'post_author', 'posted_at', 'disapproved']
    list_display_links = ['id', 'post_comment']
    list_editable = ['disapproved']
    list_filter = ['posted_at', 'disapproved']


class disapprovedfilter(admin.SimpleListFilter):
    title = 'Disapproved'
    parameter_name = 'Disapproved'

    def lookups(self, request, model_admin):
        return [
            ('False', 'false')
        ]
    
    def queryset(self, request, queryset:QuerySet):
        if self.value() == 'False':
            return queryset.filter(disapproved=False)