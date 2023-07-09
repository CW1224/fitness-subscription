from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

def show_blogs(request):
    """ A view to show the user's product reviews """
    blogs = Blog.objects.all()

    template = 'blogs/blogs.html'

    context = {
        'blogs': blogs,
    }

    return render(request, template, context)

def show_my_blogs(request):
    """ A view to show the user's product reviews """
    blogs = Blog.objects.filter(blog_author=request.user)

    template = 'blogs/my_blogs.html'

    context = {
        'blogs': blogs,
    }

    return render(request, template, context)

@login_required
def add_blog(request):

    """ Add blog  """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.blog_author = request.user
            blog=form.save()
            messages.success(request, 'Successfully added blog!')

            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blogs/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_blog(request, blog_id):
    # Form that will allow user to edit review
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.user != blog.blog_author:
        messages.error(request, 'Only the author of the blog can edit this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your blog!')

            return redirect(reverse('home'))

        else:
            messages.error(request, 'Failed to update your review. \
                Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing your review for \
            {blog.blog_author}')

    template = 'blogs/edit_blog.html'

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)

@login_required
def delete_blog(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)

    if request.user != review.author:
        messages.error(request, 'Only the author of the blog can edit this')
        return redirect(reverse('home'))

    """ Delete blog of the user """

    blog.delete()
    messages.success(request, 'Blog deleted!')

    return redirect(reverse('home'))
