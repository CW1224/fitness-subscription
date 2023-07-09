from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_blogs, name='blog'),
    path("my_blogs/", views.show_my_blogs, name='my_blog'),
    path("add_blog/", views.add_blog, name='add_blog'),
    path("edit_blog/<int:blog_id>", views.edit_blog, name='edit_blog'),
    path("delete_blog/<int:blog_id>", views.delete_blog, name='delete_blog'),
]