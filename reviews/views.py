from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


def show_reviews(request):
    """ A view to show the user's product reviews """
    reviews = Review.objects.filter(author=request.user)

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    product = get_object_or_404(Product, pk=product_id)
    user_review = Review.objects.filter(
        author=request.user, product=product)

    # Check if the user has already submitted a review for the product

    if user_review:
        messages.error(request, 'You have already submitted a review for this product')
        return redirect(reverse('product_detail', args=[product.id]))
    else:

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


@login_required
def edit_review(request, review_id):
    # Form that will allow user to edit review
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.author:
        messages.error(request, 'Only the author of the review can edit this')
        return redirect(reverse('product_detail', args=[review.product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your review!')

            update_product_rating(review.product)

            return redirect(reverse('product_detail',
                            args=[review.product.id]))

        else:
            messages.error(request, 'Failed to update your review. \
                Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review for \
            {review.product.name}')

    template = 'reviews/edit_review.html'

    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.author:
        messages.error(request, 'Only the author of the review can edit this')
        return redirect(reverse('product_detail', args=[review.product.id]))

    """ Delete review of the user """

    review.delete()
    messages.success(request, 'Review deleted!')

    return redirect(reverse('product_detail', args=[review.product.id]))


def update_product_rating(product):
    """ Update the rating field for the product """

    total_reviews = Review.objects.filter(product=product)
    number_of_total_reviews = total_reviews.count()
    ratings_sum = 0

    if number_of_total_reviews <= 0:
        product.rating = None
    else:
        for review in total_reviews:
            ratings_sum += review.rating

        product.rating = ratings_sum / number_of_total_reviews

    product.save()
