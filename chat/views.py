import os

from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name = '../templates/chat/chat.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'websocket_endpoint': os.getenv('WEBSOCKET_ENDPOINT'),
            'ip_geo_url': os.getenv('IP_GEO_URL')
        })
