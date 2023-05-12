from django.urls import path
from django.views.decorators.cache import cache_page

from home.views import HomeView, ProfileView

urlpatterns = [
    path("", cache_page(3600 * 6)(HomeView.as_view()), name="home"),
    path('profile/', ProfileView.as_view(), name='profile'),
]
