from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return to index page"""

    return render(request, 'home/index.html')

def about(request):
    """ A view to return to index page"""

    return render(request, 'home/about.html')

def contact(request):
    """ A view to return to index page"""

    return render(request, 'home/contact.html')