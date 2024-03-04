
from django.urls import path
from . import views

"""

:Routes

- Rutas para al aplicación no 3

:type list pats

    path = ({url}, {function}, {name})

    admin = vista del formulario para acceder

"""
urlpatterns = [
    path("public", views.postContent, name="page-posts-public"),
]
