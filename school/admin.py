from django.contrib import admin
from .models import Teacher


# Modelo de admin
class TeacherAdmin(admin.ModelAdmin):
    # Lista de los columnas que aparecerán
    list_display = (
        "name",
        "key",
        "date_time_create",
    )

    # Filtros de la barra de búsqueda
    search_fields = (
        "name",
        "key",
    )

    # Filtros derechos
    list_filter = (
        "category",
        "subjects",
    )

    # Filtro para la gerarquia de fechas
    # date_hierarchy = "date_time_created"


# Modelos para administración
admin.site.register(Teacher, TeacherAdmin)
