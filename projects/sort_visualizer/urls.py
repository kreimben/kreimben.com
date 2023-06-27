from django.urls import path

from projects.sort_visualizer import views

urlpatterns = [
    path('', views.SortVisualizerView.as_view(), name='sort_visualizer'),
]
