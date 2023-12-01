# from allauth.socialaccount.models import SocialAccount
from django.http import HttpRequest
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView


class BaseTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        self.object = []
        context = super().get_context_data(**kwargs)
        return context


class BaseDetailView(BaseTemplateView, DetailView):
    """
    Just for convenience.
    """


class BaseFormView(BaseTemplateView, FormView):
    """
    Just for convenience.
    """


class HomeView(BaseTemplateView):
    template_name = "index.html"

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)
