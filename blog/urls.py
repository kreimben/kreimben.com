from django.urls import path

from .views import BlogPostDetailView, BlogView, PostSearchView, BlogFileDownloadCounterView

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("post/<int:post_id>/", BlogPostDetailView.as_view(), name="post"),
    path('post/<int:post_id>/to/<str:ip>/download/<int:file_id>/', BlogFileDownloadCounterView.as_view(), name='file_download'),
    path("search/", PostSearchView.as_view(), name="search"),
]
