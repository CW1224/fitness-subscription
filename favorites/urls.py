from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_favorite, name='favorites'),
    path("add_favorite/<int:product_id>/", views.add_or_remove_favorite, name='add_favorite'),
]