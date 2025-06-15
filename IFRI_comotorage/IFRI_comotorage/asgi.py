"""
ASGI config for IFRI_comotorage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IFRI_comotorage.settings')
django.setup()  # <- Ceci doit venir avant l'import de toute app Django

from django.core.asgi import get_asgi_application
import messaging_app.routing  # <- À importer maintenant, après setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            messaging_app.routing.websocket_urlpatterns
        )
    ),
})