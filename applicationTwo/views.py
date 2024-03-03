from django.shortcuts import render

"""

:comentsContent - contenedor de comentarios

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def comentsContent(request):
    return render(request, "coments/coments-page.html", {})