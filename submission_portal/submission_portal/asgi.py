"""
ASGI config for submission_portal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path
from coursemanager import consumers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'submission_portal.settings')

application = get_asgi_application()

ws_pattern= [
    path('ws/notify', consumers.NotificationConsumer.as_asgi()),
    path('ws/instructorNotify', consumers.InstructorNotificationConsumer.as_asgi()),
]

application= ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
    }
)