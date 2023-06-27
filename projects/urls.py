from django.urls import path, include

from projects import views

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('image_to_ascii_art/', include('projects.image_to_ascii_art.urls')),
    path('sort_visualizer/', include('projects.sort_visualizer.urls')),
]
