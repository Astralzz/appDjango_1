from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Validator
phone_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="El número de teléfono debe tener exactamente 10 dígitos.",
)

key_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="La key del maestro debe tener exactamente 8 dígitos.",
)


# SECTION - Categoría maestro
class TeacherCategory(models.Model):
    # Nombre
    name = models.CharField(max_length=120, unique=True)
    # Descripción
    description = models.TextField(max_length=1000, null=True)
    # Fecha y hora
    date_time_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# SECTION - Materia
class Subject(models.Model):
    # Nombre
    name = models.CharField(max_length=120, unique=True)
    # Descripción
    description = models.TextField(max_length=1000, null=True)
    # Fecha y hora
    date_time_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# SECTION - Maestro
class Teacher(models.Model):
    # Categoría
    category = models.ForeignKey(
        TeacherCategory, on_delete=models.CASCADE, related_name="teachers"
    )
    # Nombre
    name = models.CharField(max_length=120)
    # Clave
    key = models.CharField(max_length=8, unique=True, validators=[key_validator])
    # Materias que enseña | Relación muchos a muchos
    subjects = models.ManyToManyField(Subject, related_name="teachers")
    # Fecha y hora
    date_time_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# SECTION - Detalle de maestro
class TeacherDetail(models.Model):
    # Maestro | Relación 1:1
    teacher = models.OneToOneField(
        Teacher, on_delete=models.CASCADE, related_name="detail"
    )
    # Email
    email = models.EmailField(unique=True)
    # Teléfono
    phone = models.CharField(max_length=10, null=True, validators=[phone_validator])
    # Dirección
    direction = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.teacher.name
