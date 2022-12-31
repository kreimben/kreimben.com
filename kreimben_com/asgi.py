import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kreimben_com.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

from chat.consumers import ChatConsumer

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter([path('ws/chat/', ChatConsumer.as_asgi())]))
    )
})
