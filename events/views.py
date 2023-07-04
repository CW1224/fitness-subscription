from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# Create your views here.

def show_events(request):
    """ A view to show the user's product reviews """

    events = Event.objects.all()

    template = 'events/events.html'

    context = {

        'events': events
    }

    return render(request, template, context)

@login_required
def add_event(request):

    """ Add an event """
    """ Check if the user is a superuser or not """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event=form.save()
            messages.success(request, 'Successfully added event!')

            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }
    return render(request, template, context)