import os

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("home.urls")),
    path("blog/", include("blog.urls")),
    path(f'{os.getenv("DJANGO_REAL_ADMIN_URI")}/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
