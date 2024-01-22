from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'slug', 'created_at']
    list_filter = ['created_at']

admin.site.register(Article, ArticleAdmin)
