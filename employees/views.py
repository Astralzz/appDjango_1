from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeesForm
from .models import Employee


def getAllEmployees(orderBy="-date_time_create"):
    # Lista de empleados ordenada por ???
    return Employee.objects.all().order_by(orderBy)


def create(request):
    # ? No es POST
    if request.method != "POST":
        # ! Error
        return HttpResponse("Solo se admite solicitud POST")

    try:
        # formulario
        form = EmployeesForm(request.POST)

        # Capturar datos del formulario
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")

        # ? Datos no válidos
        if not form.is_valid():
            # ! ERROR
            raise ValueError("Error de validación")

        # Creamos
        Employee.objects.create(name=name, phone=phone, gender=gender)

        return render(
            request,
            "employees/employees-page.html",
            {
                "form": EmployeesForm(),
                "employees": getAllEmployees(),
                "success_message": "El empleado sse creo correctamente",
            },
        )

    # ! Error
    except Exception as e:
        return render(
            request,
            "employees/employees-page.html",
            {
                "form": form,
                "employees": getAllEmployees(),
                "error_message": str(e),
            },
        )


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
            "employees": getAllEmployees(),
            "form": form,
        },
    )
