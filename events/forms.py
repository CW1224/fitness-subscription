from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_title', 'content', 'event_on', 'street_address1', 'street_address2',
        'town_or_city', 'county', 'postcode')
