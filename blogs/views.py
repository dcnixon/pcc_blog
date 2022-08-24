from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import EntryForm


def index(request):
    """The home page for Blogs"""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts': blogposts}

    return render(request, 'blogs/index.html', context)


def new_entry(request):
    """Add a new blog post."""

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = BlogPost.objects.get(id=entry_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'entry': entry, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)
