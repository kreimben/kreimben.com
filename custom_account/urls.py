from allauth.socialaccount.providers.google.views import oauth2_callback, oauth2_login
from django.urls import path

from .views import CustomLogoutView, CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name='account_login'),
    path("logout/", CustomLogoutView.as_view(), name='account_logout'),
    path('google/login/', oauth2_login, name='google_login'),
    path('google/login/callback/', oauth2_callback, name='google_callback'),
]
