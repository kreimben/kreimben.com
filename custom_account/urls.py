from django.urls import path

from .views import CustomLogoutView

urlpatterns = [
    path("_account/logout/", CustomLogoutView.as_view(), name="custom_account_logout"),
]
