"""
Configuración ASGI para el proyecto AppDjango_1.

Expone el ASGI llamable como una variable a nivel de módulo llamada `` Aplicación ''.

Para obtener más información sobre este archivo, consulte

#LINK -  https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appDjango_1.settings')

application = get_asgi_application()
