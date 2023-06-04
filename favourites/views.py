from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_favourites(request):
    """ A view that renders the bag contents"""

    favorite_products = Product.objects.filter(users_favorite=request.user)

    context = {
        'favorite_products': favorite_products,
    }

    return render(request, 'favourites/favourites.html')

def add_to_favorites(request, item_id):
    """ Add product to the user's favorites """
    product = get_object_or_404(Product, id=item_id)

    if product.users_favorite.filter(id=request.user.id).exists():
        product.users_favorite.remove(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         removed from your favorites.')
    else:
        product.users_favorite.add(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         added to your favorites.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))