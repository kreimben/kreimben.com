from django.http import HttpRequest
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, **kwargs):
        context = {

        }
        return self.render_to_response(context)
