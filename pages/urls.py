from django.urls import path

from .views import home_view, about_view, contact_view, services_view

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('services/', services_view),
]
