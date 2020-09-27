from django.shortcuts import render

site_name = "Stylus Photography"


def home_view(request):
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'home.html', context)


def gallery_view(request):
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'gallery.html', context)


def services_view(request):
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'services.html', context)


def about_view(request):
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'about.html', context)


def contact_view(request):
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'contact.html', context)
