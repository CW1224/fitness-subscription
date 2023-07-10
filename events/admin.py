from django.contrib import admin
from .models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_title', 'content', 'event_on', 'location'
    )

    ordering = ('-created_on',)


admin.site.register(Event, EventAdmin)
