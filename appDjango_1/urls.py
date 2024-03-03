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
    1. Importar la función incluir (): desde django.urls import include, ruta
    2. Agregue una URL a UrlPatherns: Path ('Blog/', incluya ('Blog.urls')))
"""

from django.contrib import admin
from django.urls import path, include

from appDjango_1 import views

"""

:Routes

- Rutas por defecto de la app

:type list pats

    path = ({url}, {function}, {name})

    admin = vista del formulario para acceder
    dataOne = vista de dato normal 
    dataTwo = vista de datos enviando parámetros en las urls

"""
urlpatterns = [
    path("", views.index, name="index"),
    # Admin
    path("admin/", admin.site.urls),
    # Retornar HttpResponse básico
    path("basic/data/", views.dataOne, name="basic-data"),
    path("basic/user/<str:name>/<int:edad>", views.dataUser, name="basic-user"),
    # Retornar views
    path("views/basic/one", views.basicViewOne, name="views-basic-one"),
    path(
        "views/basic/two/<str:name>/<int:edad>",
        views.basicViewTwo,
        name="views-basic-two",
    ),
    # Retornar views layout
    path("layout/one", views.pageOneLayout, name="layouts-page-one"),
    path("layout/two", views.pageTwoLayout, name="layouts-page-two"),
    path("layout/three", views.pageThreeLayout, name="layouts-page-three"),
    # Rutas de aplicationTwo
    path("page/coments", include("applicationTwo.urls")),
]
