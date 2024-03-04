import random
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction
from .models import TeacherCategory, Subject, Teacher, TeacherDetail

"""

:getRandomTeacherCategory - Obtener una categoría aleatoria

:return TeacherCategory

"""


def getRandomTeacherCategory():
    # Obtenemos todas las categorías de maestros disponibles
    all_categories = TeacherCategory.objects.all()

    # Retornamos una categoría aleatoria
    return random.choice(all_categories)


"""

:createTeacher - Crear maestro

:param request:Any

:return void

"""


def createTeacherFormHtml(request):
    # ? Es POST
    if request.method == "POST":
        try:
            # Capturar datos del formulario
            email = request.POST.get("email")
            name = request.POST.get("name")
            category_id = request.POST.get("category")
            phone = request.POST.get("phone")
            direction = request.POST.get("direction")

            # Validar datos del formulario
            if not email or not name or not category_id or not phone or not direction:
                messages.error(request, "Por favor, complete todos los campos.")
                return HttpResponse("Por favor, complete todos los campos.")

            # Obtener la categoría de maestro correspondiente
            category = TeacherCategory.objects.get(id=category_id)

            # Verificar si el email ya está registrado
            if TeacherDetail.objects.filter(email=email).exists():
                messages.error(request, "El email ya se encuentra registrado.")
                return HttpResponse("El email ya se encuentra registrado.")

            # Creamos en transition para poner los 2 si o si
            with transaction.atomic():
                # Generamos key
                key = getKeyTeacherUnique()

                # Creamos maestro
                teacher = Teacher.objects.create(category=category, name=name, key=key)

                # Creamos detalles
                TeacherDetail.objects.create(
                    teacher=teacher,
                    email=email,
                    phone=phone,
                    direction=direction,
                )

            # Mensaje de éxito y redirection a la misma página
            messages.success(request, "¡Maestro creado con éxito!")
            return HttpResponse("Se creo el maestro correctamente")

        # ! Error
        except Exception as e:
            # Manejo de errores generales
            messages.error(request, f"Ocurrió un error: {str(e)}")
            return HttpResponse(f"Ocurrió un error: {str(e)}")

    # No es una solicitud POST
    messages.error(request, "Solo se admite solicitud POST")
    return HttpResponse("Solo se admite solicitud POST")


"""

:getKeyTeacherUnique - Generar key única

:return key:number

"""


def getKeyTeacherUnique():
    # Generar una clave única de 8 dígitos
    key = "".join(random.choices("0123456789", k=8))
    # Recorremos asta que sea única
    while Teacher.objects.filter(key=key).exists():
        key = "".join(random.choices("0123456789", k=8))
    return key


"""

:addSubjectInTeacher - Agregar n materias a n profesores

:param n:number
:param type:add|remove 

:return void

"""


def addRemoveSubjectInTeacher(n, type="add"):
    # Obtenemos datos
    all_subjects = Subject.objects.all()
    all_teachers = Teacher.objects.all()

    # Verificar si hay suficientes datos para relacionar
    if len(all_subjects) == 0 or len(all_teachers) == 0:
        print("No hay suficientes maestros o materias disponibles.")
        return

    # Seleccionamos n maestros aleatorios
    selected_teachers = random.sample(list(all_teachers), n)

    # Recorremos
    for teacher in selected_teachers:
        # Seleccionamos n materias aleatorias
        selected_subjects = random.sample(list(all_subjects), n)

        # ? Agregar
        if type == "add":
            # Asignar las materias a los maestros seleccionados
            teacher.subjects.add(*selected_subjects)
            print(f"Se han agregado {n} materias a {teacher.name}.")

        # ? Eliminar
        elif type == "remove":
            # Eliminar las materias de los maestros seleccionados
            teacher.subjects.remove(*selected_subjects)
            print(f"Se han eliminado {n} materias de {teacher.name}.")

        else:
            print("Tipo no válido. Debe ser 'add' o 'remove'.")


"""

:schoolContent - contenedor de maestros

:param request:Any

:render - render({request}, {template/vista}, {content/datos})

:return render view

"""


def schoolContent(request):
    # Creamos
    # createTeacherFormHtml(request)

    # Creamos relaciones m:m
    addRemoveSubjectInTeacher(random.randint(5, 10))

    # Lista de maestros ordenada por key
    teachers = Teacher.objects.all().order_by("key")

    # Lista de maestros de id=1 categoría ordenada por key
    # teachers = getRandomTeacherCategory().teachers.all().order_by("key")

    # Lista de categorías de maestros
    teacherCategorys = TeacherCategory.objects.all().order_by("name")

    return render(
        request,
        "school/school-page.html",
        {"teachers": teachers, "teacherCategorys": teacherCategorys},
    )
