"""
ASGI config for IFRI_comotorage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import messagerie.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IFRI_comotorage.settings')


application = ProtocolTypeRouter({
    # on branche le protocole WebSocket
    'websocket': AuthMiddlewareStack(
        URLRouter(
            messagerie.routing.websocket_urlpatterns
        )
    ),
})


application = get_asgi_application()
