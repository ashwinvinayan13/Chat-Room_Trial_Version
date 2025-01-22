from django.urls import re_path
from chat import consumers

websocket_urlpatterns = [
    re_path('ws/socket-server/', consumers.ChatConsumer.as_asgi())
]