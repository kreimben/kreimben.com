import os

from django.contrib import admin
from django.urls import include, path

from server_error.views import ServerErrorView

urlpatterns = [
    path("", include("home.urls")),
    path("blog/", include("blog.urls")),
    path('projects/', include('projects.urls')),

    path(f'{os.getenv("DJANGO_REAL_ADMIN_URI")}/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('custom_account.urls')),
]

if os.getenv("DJANGO_DEBUG") == "True":
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

handler500 = ServerErrorView.as_view()
