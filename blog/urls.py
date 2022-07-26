from django.urls import path
from .views import BlogView, BlogPostDetailView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:post_id>', BlogPostDetailView.as_view(), name='post')
]
