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

def event_detail(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_detail.html', context)

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

            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_event(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('events'))

    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_detail', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)