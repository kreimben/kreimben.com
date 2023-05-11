import json
import os

from home.views import BaseTemplateView


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ChatView(BaseTemplateView):
    template_name = '../templates/chat/chat.html'

    def get(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        return self.render_to_response({
            'websocket_endpoint': os.getenv('WEBSOCKET_ENDPOINT'),
            'ip': json.dumps({'ip': ip})
        })
