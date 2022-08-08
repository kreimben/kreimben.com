from django.urls import path

from .views import BlogView, BlogPostDetailView, PostSearchView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:post_id>', BlogPostDetailView.as_view(), name='post'),
    path('search/', PostSearchView.as_view(), name='search'),
]
