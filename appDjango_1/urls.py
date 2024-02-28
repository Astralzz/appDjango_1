"""
Configuración de URL para el proyecto AppDJango_1.

La lista de `` Urlpaterns 'enruta las URL a las vistas.Para obtener más información, consulte:
    #LINK -  https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Vistas de funciones
    1. Agregue una importación: desde las vistas de importación my_app
    2. Agregue una URL a UrlPatterns: Path ('', Views.Home, Name = 'Home')
Vistas basadas en clases
    1. Agregue una importación: desde otro_app.views Import Home
    2. Agregue una URL a UrlPatterns: Path ('', home.as_view (), name = 'Home')
Incluyendo otro urlconf
    1. Importar la función incluir (): desde django.urls import incluir, ruta
    2. Agregue una URL a UrlPatherns: Path ('Blog/', incluya ('Blog.urls')))
"""
from django.contrib import admin
from django.urls import path

from appDjango_1 import views

"""

:Routes

- Rutas por defecto de la app

:type list

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dataOne/', views.dataOne, name='data-one'),
]
