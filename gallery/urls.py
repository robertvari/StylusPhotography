from django.urls import path

from .views import GalleryView, PhotoDetailsView

urlpatterns = [
    path('', GalleryView.as_view(), name="gallery_home"),
    path('<str:slug>/', PhotoDetailsView.as_view(), name="photo_details")
]