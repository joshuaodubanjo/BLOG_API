from django.db import models
from django.core.validators import MinLengthValidator

from user.models import CustomUser, Profile

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    publish = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=250)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='author')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.first_name
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author', default=True)
    published = models.BooleanField(default=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='tag')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    posted_at = models.DateField(auto_now_add=True)
    disapproved = models.BooleanField(default=False)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='commentator')

    def post_author(self):
        return self.author
    
    def post_id(self):
        return self.post.id

    def post_comment(self):
        return self.post.title

    def __str__(self):
        return f'Comment for {self.post.title}'