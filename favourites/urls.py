from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favourites, name='view_favourites'),
    path('add_favourite/<item_id>/', views.add_to_favorites, name='add_to_favorites'),
]