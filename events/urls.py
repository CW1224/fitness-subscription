from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_events, name='events'),
    path('event_detail/<int:event_id>', views.event_detail, name='event_detail'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:event_id>', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
]
