from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils import timezone

# Validator
phone_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="El número de teléfono debe tener exactamente 10 dígitos.",
)


# SECTION - Autor
class Autor(models.Model):
    # Nombre
    name = models.CharField(max_length=120)
    # Email
    email = models.EmailField(unique=True)
    # Teléfono
    phone = models.CharField(max_length=10, null=True, validators=[phone_validator])
    # Descripción
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name


# SECTION - Post
class Post(models.Model):
    # Autor
    author = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")

    # Título
    title = models.CharField(max_length=255, unique=True)

    # Texto
    text = models.TextField(max_length=5000, validators=[MinLengthValidator(5)])

    # Texto
    comment = models.TextField(
        max_length=700, null=True, validators=[MinLengthValidator(5)]
    )

    # Fecha y hora
    date_time_create = models.DateTimeField(default=timezone.now)
