"""
ASGI config for catering_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from channels.security.websocket import AllowedHostsOriginValidator

import main.routing  # Import routing for the WebSocket app

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catering_website.settings')

# application = get_asgi_application({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             main.routing.websocket_urlpatterns
#         )
#     ),
# })

# Define ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                main.routing.websocket_urlpatterns
            )
        )
    ),
})
