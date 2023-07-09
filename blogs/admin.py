from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'blog_author',
        'content',
        'created_on',
        'image_url',
        'image'
    )

    ordering = ('-created_on',)


admin.site.register(Blog, BlogAdmin)