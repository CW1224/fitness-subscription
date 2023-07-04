from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_events, name='events'),
    path('add_event/', views.add_event, name='add_event'),
]