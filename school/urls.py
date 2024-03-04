
from django.urls import path
from . import views

"""

:Routes

- Rutas para al aplicación no 4

:type list pats

    path = ({url}, {function}, {name})

"""
urlpatterns = [
    path("public", views.schoolContent, name="page-school-public"),
]
