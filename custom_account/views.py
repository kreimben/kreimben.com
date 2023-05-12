from allauth.account.adapter import get_adapter
from allauth.account.utils import get_next_redirect_url
from allauth.account.views import LogoutFunctionalityMixin, _ajax_response
from allauth.utils import get_request_param
from django.shortcuts import redirect

from home.views import BaseTemplateView


class CustomLogoutView(LogoutFunctionalityMixin, BaseTemplateView):
    template_name = "allauth/account/logout.html"
    redirect_field_name = "next"

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            response = redirect(self.get_redirect_url())
            return _ajax_response(self.request, response)
        ctx = self.get_context_data()
        response = self.render_to_response(ctx)
        return _ajax_response(self.request, response)

    def post(self, *args, **kwargs):
        url = self.get_redirect_url()
        if self.request.user.is_authenticated:
            self.logout()
        response = redirect(url)
        return _ajax_response(self.request, response)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        redirect_field_value = get_request_param(self.request, self.redirect_field_name)
        ctx.update(
            {
                "redirect_field_name": self.redirect_field_name,
                "redirect_field_value": redirect_field_value,
            }
        )
        return ctx

    def get_redirect_url(self):
        return get_next_redirect_url(
            self.request, self.redirect_field_name
        ) or get_adapter(self.request).get_logout_redirect_url(self.request)
