from django.shortcuts import render
from .forms import EmployeesForm


def create(request):
 pass

"""

:employeesContent - contenedor de empleados

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def employeesContent(request):
    # Formulario
    form = EmployeesForm()

    return render(
        request,
        "employees/employees-page.html",
        {
            "form": form,
        },
    )
