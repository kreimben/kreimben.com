from django.urls import path

from projects.image_to_ascii_art.views import ImageToAsciiView, ImageConvertingResultView, \
    ImageConvertingResultDetailView

urlpatterns = [
    path('', ImageToAsciiView.as_view(), name='image_to_ascii_art_view'),
    path('converting_result/', ImageConvertingResultView.as_view(), name='converting_result'),
    path('converting_result/<int:pk>/', ImageConvertingResultDetailView.as_view(), name='converting_result_detail'),
]
