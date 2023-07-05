from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_title', 'content', 'event_on', 'street_address1', 'street_address2',
        'town_or_city', 'county', 'postcode'
    )

    ordering = ('-created_on',)


admin.site.register(Event, EventAdmin)