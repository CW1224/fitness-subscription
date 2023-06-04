from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favourites, name='view_favourites'),
    path('add_favourite/<item_id>/', views.add_to_favorites, name='add_to_favorites'),
    #path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    #path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]