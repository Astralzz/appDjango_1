"""
WSGI config for appDjango_1 project.

Expone el WSGI llamable como una variable a nivel de módulo llamada `` Aplicación ''.

Para obtener más información sobre este archivo, consulte
#LINK -  https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appDjango_1.settings')

application = get_wsgi_application()
