from django.shortcuts import render, HttpResponse


def home_view(request):
    return HttpResponse('Home page')


def about_view(request):
    return HttpResponse("About page")


def contact_view(request):
    return HttpResponse("Contact page")
