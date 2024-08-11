from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/solicitudes/$', consumers.SolicitudConsumer.as_asgi()),
]