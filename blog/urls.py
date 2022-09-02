from django.urls import path

from .views import BlogPostDetailView, BlogView, PostSearchView

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("post/<int:post_id>", BlogPostDetailView.as_view(), name="post"),
    path("search/", PostSearchView.as_view(), name="search"),
]
