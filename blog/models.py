from django.db import models
from django.db.models import F

from main.settings import AUTH_USER_MODEL

def makeSlug(title):
    title = str(title)
    n,m = title.lower().split(' '), ''
    for x in n:
        if x == '':
            n.pop(n.index(x))
    for x in range(len(n)):
        if x != 0:
            m = f'{m}_{n[x]}'
        else:
            m = n[0]
    return m


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    tags = models.TextField()

    def __str__(self) -> str:
        return self.title  

    def get_absolute_url(self):
        return '/%s/' % self.slug
    
    class Meta:
        ordering = ['-created_at']
