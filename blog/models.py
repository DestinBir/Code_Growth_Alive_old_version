"""from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
# from embed_video.fields import EmbedVideoField

from main.settings import AUTH_USER_MODEL

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    

    class Meta:
        ordering = ('-title',)
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug 

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    intro = models.TextField()
    body = CKEditor5Field('Text', config_name='extends', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=DRAFT)
    link = models.URLField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='categories', on_delete=models.CASCADE)

    prepopulated_fields = {'slug': ('title',)}

    def __str__(self) -> str:
        return self.title

    def total_likes(self):
        return self.likes.count()    

    def get_absolute_url(self):
        return '/%s/' % self.slug
    
    class Meta:
        ordering = ['-created_at']
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-post',)

"""