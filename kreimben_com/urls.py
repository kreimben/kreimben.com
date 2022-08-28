import os

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("home.urls")),
    path("blog/", include("blog.urls")),
    path("products/", include("products.urls")),
    path(f'{os.getenv("DJANGO_REAL_ADMIN_URI")}/', admin.site.urls),
]
