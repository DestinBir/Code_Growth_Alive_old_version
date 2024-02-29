# from ckeditor.fields import RichTextField
from mdeditor.fields import MDTextField
from django.db import models
# from embed_video.fields import EmbedVideoField
from main.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    class Lang(models.TextChoices):
        FR = "Fr", "Fr"
        EN = "En", "En"

    lang_role = Lang.FR

    langue = models.CharField(_('language'), max_length=20, choices=Lang.choices)
    titre = models.CharField(_('title'), max_length=255)
    theme = models.CharField(_('tag'), max_length=500)
    slug = models.SlugField(_('slug'), blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='article', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='articles')


    prepopulated_fields = {'slug': ('titre',)}

    def __str__(self) -> str:
        return self.title

    def total_likes(self):
        return self.likes.count()    

    def get_absolute_url(self):
        return '/%s/' % self.slug
    
    class Meta:
        ordering = ('-created_at',)
    
class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    personne = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.post.titre} - {self.personne.username}"

    class Meta:
        ordering = ('-post',)

