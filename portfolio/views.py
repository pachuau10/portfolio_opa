from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GalleryItem, Experience, Skill
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect(request.path + '#contact')
        else:
            messages.error(request, 'Please correct the errors and try again.')
    else:
        form = ContactForm()

    context = {
        'gallery_items': GalleryItem.objects.all()[:9],
        'experiences': Experience.objects.all(),
        'skills': Skill.objects.all(),
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)


def gallery_detail(request, pk):
    item = get_object_or_404(GalleryItem, pk=pk)
    related = GalleryItem.objects.exclude(pk=pk).filter(category=item.category)[:3]
    return render(request, 'portfolio/gallery_detail.html', {
        'item': item,
        'related': related,
    })