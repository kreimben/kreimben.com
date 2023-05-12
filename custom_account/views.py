from allauth.account.adapter import get_adapter
from allauth.account.forms import LoginForm
from allauth.account.utils import get_next_redirect_url, passthrough_next_redirect_url
from allauth.account.views import LogoutFunctionalityMixin, _ajax_response, RedirectAuthenticatedUserMixin, \
    AjaxCapableProcessFormViewMixin
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_request_param
from django.contrib.auth.admin import sensitive_post_parameters_m
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from home.views import BaseTemplateView


class CustomLoginView(
    RedirectAuthenticatedUserMixin, AjaxCapableProcessFormViewMixin, FormView, BaseTemplateView
):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = None
    redirect_field_name = "next"

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CustomLoginView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    # def get_form_class(self):
    #     return get_form_class(app_settings.FORMS, "login", self.form_class)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
                get_next_redirect_url(self.request, self.redirect_field_name)
                or self.success_url
        )
        return ret

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        signup_url = passthrough_next_redirect_url(
            self.request, reverse("account_signup"), self.redirect_field_name
        )
        redirect_field_value = get_request_param(self.request, self.redirect_field_name)
        site = get_current_site(self.request)

        ret.update(
            {
                "signup_url": signup_url,
                "site": site,
                "redirect_field_name": self.redirect_field_name,
                "redirect_field_value": redirect_field_value,
            }
        )
        return ret


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
