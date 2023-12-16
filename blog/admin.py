from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin, )
