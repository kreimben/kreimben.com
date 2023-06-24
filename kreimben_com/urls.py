import os

from django.contrib import admin
from django.urls import include, path

from server_error.views import ServerErrorView

urlpatterns = [
    path("", include("home.urls")),
    path("blog/", include("blog.urls")),
    path('chat/', include('chat.urls')),
    path('image_to_ascii_art/', include('image_to_ascii_art.urls')),

    path(f'{os.getenv("DJANGO_REAL_ADMIN_URI")}/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('custom_account.urls')),
]

handler500 = ServerErrorView.as_view()
