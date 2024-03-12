from django.urls import path

from . import views

urlpatterns = [
    path('', views.YourModelDetailView.as_view(), name='mnist_classifier'),
]
