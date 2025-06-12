from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # regex pour capturer le paramètre <room_name>
    # en principe on emploi path pour récuoerer les url mais re_path est plus adapté pour l'extraction
    # du room_name dont on a besoin dans le Chatconsumer
    # au cas où, renseignez-vous sur l'importance du regex à ce niveau
    re_path(r'ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi()),
]