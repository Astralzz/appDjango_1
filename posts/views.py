from django.shortcuts import render
from .models import Autor

"""

:updateAutor - Actualizar autor

:param request:Any

:return void

"""


def updateAutor(request):
    # Obtenemos autor
    autorById = Autor.objects.get(id=10)

    autorById.name = "Edain Jesus CC"
    autorById.email = "daiinx@gmail.com"
    autorById.phone = "7474152450"
    autorById.description = "Ing en computación y desarrollador full stack"
    autorById.save()


"""

:postContent - contenedor de posts

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def postContent(request):
    # Actualizamos
    updateAutor(request)

    # Lista de autores
    autors = Autor.objects.all()

    # Lista de autores filtrados
    autors = Autor.objects.filter(email="jennifer90@example.org")

    # Un solo autor por id
    autorById = Autor.objects.get(id=10)

    # Lista de autores por limite [min:max]
    autors = Autor.objects.all()[6:12]

    # Lista de autores ordenada por email
    autors = Autor.objects.all().order_by("email")[10:15]

    # Lista de autores filtrados que el nombre tenga ala
    autors = Autor.objects.filter(name__contains="mor").order_by("email")

    # Lista de autores filtrados que la id sea menor o igual a 14
    autors = Autor.objects.filter(id__lte=14).order_by("email")

    return render(
        request, "posts/posts-page.html", {"autors": autors, "autor_id": autorById}
    )
