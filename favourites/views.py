from django.shortcuts import render

# Create your views here.

def view_favourites(request):
    """ A view that renders the bag contents"""

    return render(request, 'favourites/favourites.html')