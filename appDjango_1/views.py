from django.http import HttpResponse
from django.shortcuts import render


# SECTION - INDEX

"""

:basicViewOne - url index

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def index(request):
    return render(request, "index.html", {})


# SECTION - BASIC

"""

:dataOne - url numero 1 - cadena básica

:param request:Any

:return HttpResponse

"""


def dataOne(request):
    return HttpResponse("Hola mundo")


"""

:dataOne - url numero 2 - datos básicos de usuario

:param request:Any
:paran name:str
:param edad:int

:return HttpResponse

"""


def dataUser(request, name, edad):
    # ? No es nulo
    if edad is not None:
        # ? Mayor o igual a 18 y menor a 121
        if edad >= 18 and edad <= 121:
            edad_text = "mayor de edad"
        # ? Mayor o igual a 1 y menor a 18
        elif edad >= 1 and edad < 18:
            edad_text = "menor de edad"
        else:
            edad_text = "una persona con una edad errónea"
    else:
        edad_text = "N/A"

    return HttpResponse(
        "Hola me llamo "
        + str(name if name else "N/A")
        + ", mi edad es "
        + str(edad if edad else "N/A")
        + " y soy "
        + str(edad_text)
    )


# SECTION - RENDERS BASICS

"""

:basicViewOne - url numero 3 - vista no 1

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def basicViewOne(request):
    return render(request, "basic/view-one.html", {})


"""

:basicViewTwo - url numero 4 - vista no 2 dinámica

:param request:Any
:param name:str

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def basicViewTwo(request, name, edad):
    # Lista
    lista = ["Manzana", "Coco", "Pera", "Mango", "Papaya", "Durazno"]

    # Contexto
    context = {"name": name, "edad": edad, "list": lista}

    return render(request, "basic/view-two.html", context)


# SECTION - RENDERS LAYOUTS BASIC
"""

:pageOneLayout - url numero 5 - vista layout no 1

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def pageOneLayout(request):
    return render(request, "layout/page-one.html", {})


"""

:pageTwoLayout - url numero 6 - vista layout no 2

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def pageTwoLayout(request):
    return render(request, "layout/page-two.html", {})


"""

:pageThreeLayout - url numero 7 - vista layout no 3

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def pageThreeLayout(request):
    return render(request, "layout/page-three.html", {})
