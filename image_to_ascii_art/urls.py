from django.urls import path

from image_to_ascii_art.views import ImageToAsciiView

urlpatterns = [
    path('', ImageToAsciiView.as_view(), name='image_to_ascii_art_view'),
]
