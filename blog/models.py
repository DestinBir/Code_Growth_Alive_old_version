# from ckeditor.fields import RichTextField
from mdeditor.fields import MDTextField
from django.db import models
# from embed_video.fields import EmbedVideoField
from main.settings import AUTH_USER_MODEL

class Article(models.Model):
    language = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, null=True)
    content = MDTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='article', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True, upload_to='articles')


    prepopulated_fields = {'slug': ('title',)}

    def __str__(self) -> str:
        return self.title

    def total_likes(self):
        return self.likes.count()    

    def get_absolute_url(self):
        return '/%s/' % self.slug
    
class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-post',)

