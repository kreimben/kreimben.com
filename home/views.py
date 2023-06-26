from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView
from silk.profiling.profiler import silk_profile


class BaseTemplateView(TemplateView):
    @silk_profile(name='get_context_data')
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


class BaseFormView(BaseTemplateView, FormView):
    """
    Just for convenience.
    """


class HomeView(BaseTemplateView):
    template_name = "index.html"

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)


class ProfileView(BaseTemplateView):
    template_name = "profile/profile.html"

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data()
        context['provider'] = context['google_user'].provider
        context['profile_image'] = context['google_user'].extra_data['picture']
        return self.render_to_response(context)
