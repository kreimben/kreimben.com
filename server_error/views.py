import traceback

from django.http import HttpRequest

from home.views import BaseTemplateView
from server_error.models import ErrorStatus


class ServerErrorView(BaseTemplateView):
    template_name = 'error.html'

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data()

        # collect data
        ErrorStatus.objects.create(
            traceback=traceback.print_exc(),
            status_code=500,
            path=context['path'],
            method=context['method'],
            user_agent=context['user_agent'],
            ip_address=context['ip_address'],
        )

        return self.render_to_response(context)
