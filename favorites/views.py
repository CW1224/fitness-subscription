from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required
def show_favorite(request):
    """ A view to show the user's favorite products"""
    favorite = Product.objects.filter(user_favorite=request.user)

    context = {
        'favorite': favorite,
    }

    return render(request, 'favorites/favorites.html', context)

@login_required
def add_or_remove_favorite(request, product_id):
    """ Add product to the user's favorites """
    product = get_object_or_404(Product, id=product_id)

    if product.user_favorite.filter(id=request.user.id).exists():
        product.user_favorite.remove(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         removed from your favorites.')
    else:
        product.user_favorite.add(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         added to your favorites.')

    return redirect(reverse('product_detail', args=[product.id]))