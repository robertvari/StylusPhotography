from django.shortcuts import render
from .models import About


def home_view(request):
    return render(request, 'home.html')


def gallery_view(request):
    return render(request, 'gallery.html')


def services_view(request):
    return render(request, 'services.html')


def about_view(request):
    abouts = About.objects.all()
    context = {}
    if abouts:
        context["title"] = abouts[0].title
        context["content"] = abouts[0].content

    return render(request, 'about.html', context)


def contact_view(request):
    return render(request, 'contact.html')
