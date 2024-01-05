from django.contrib import admin
from .models import *
"""
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'slug', 'created_at']
    list_filter = ['tags', 'created_at']

admin.site.register(Post, PostAdmin)
"""