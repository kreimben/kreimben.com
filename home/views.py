from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class BaseTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        self.object = []
        context = super().get_context_data(**kwargs)
        if isinstance(self.request.user, AnonymousUser):
            context['django_user'] = None
            context['google_user'] = None
        else:
            context['django_user'] = self.request.user
            try:
                context['google_user'] = SocialAccount.objects.get(user=self.request.user)
            except SocialAccount.DoesNotExist:
                context['google_user'] = None
        return context


class BaseDetailView(BaseTemplateView, DetailView):
    """
    Just for convenience.
    """


class HomeView(BaseTemplateView):
    template_name = "index.html"

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)
