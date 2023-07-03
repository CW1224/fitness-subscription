from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def show_reviews(request):
    """ A view to show the user's product reviews """
    reviews = review.objects.filter(author=request.user)

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)

def add_review(request, product_id):
    """ Add a review to a product """
    product = get_object_or_404(Product, pk=product_id)
    user_review = Review.objects.filter(
        author=request.user, product=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'Successfully added review!')

            update_product_rating(product)

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
    }
    return render(request, template, context)

def update_product_rating(product):
    """ Update the rating field for the product """

    total_reviews = Review.objects.filter(product=product)
    numberr_of_total_reviews = total_reviews.count()
    ratings_sum = 0

    if number_of_total_reviews <= 0:
        product.rating = None
    else:
        for review in total_reviews:
            ratings_sum += review.rating

        product.rating = ratings_sum / nr_of_total_reviews

    product.save()