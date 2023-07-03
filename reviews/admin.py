from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'product',
        'created_on',
        'rating',
    )

    ordering = ('-created_on',)


admin.site.register(Review, ReviewAdmin)