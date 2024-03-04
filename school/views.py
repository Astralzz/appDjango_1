import random
from django.shortcuts import render
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


def createTeacher(request):
    # Data
    nameTeacher = "Karla Lisbeth Cortez Marquez"
    keyTeacher = "48655268"

    # Verificamos si ya existe
    existing_teacher = Teacher.objects.filter(name=nameTeacher, key=keyTeacher).exists()

    # ? Existe
    if existing_teacher:
        return

    # Creamos maestro
    teacher = Teacher(
        category=getRandomTeacherCategory(),
        name=nameTeacher,
        key=keyTeacher,
    )
    teacher.save()

    # Creamos detalles del maestro
    teacherDetail = TeacherDetail(
        teacher=teacher,
        email="karlaList12@gmail.com",
        phone="7478525666",
        direction="Calle principal, no 23, Mexico City",
    )
    teacherDetail.save()


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
    createTeacher(request)

    # Creamos relaciones m:m
    addRemoveSubjectInTeacher(random.randint(5, 10))

    # Lista de maestros ordenada por key
    teachers = Teacher.objects.all().order_by("key")

    # Lista de maestros de id=1 categoría ordenada por key
    teachers = getRandomTeacherCategory().teachers.all().order_by("key")

    return render(request, "school/school-page.html", {"teachers": teachers})
