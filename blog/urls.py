from django.urls import path
from django.views.decorators.cache import cache_page

from .views import BlogPostDetailView, BlogView, PostSearchView, BlogFileDownloadCounterView

urlpatterns = [
    path("", cache_page(3600 * 6)(BlogView.as_view()), name="blog"),
    path("post/<int:post_id>/", cache_page(3600 * 6)(BlogPostDetailView.as_view()), name="post"),
    path('post/<int:post_id>/to/<str:ip>/download/<int:file_id>/', BlogFileDownloadCounterView.as_view(),
         name='file_download'),
    path("search/", PostSearchView.as_view(), name="search"),
]
