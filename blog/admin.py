from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['titre', 'body']
    list_display = ['titre', 'slug', 'created_at']
    list_filter = ['created_at']

admin.site.register(Article, ArticleAdmin)
