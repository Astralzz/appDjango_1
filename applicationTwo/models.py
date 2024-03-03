from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


# Modelo notas
class Notes(models.Model):
    # Titulo
    title = models.CharField(max_length=255, unique=True)

    # Texto
    text = models.TextField(
        max_length=3000, null=False, validators=[MinLengthValidator(5)]
    )

    # Puntuación
    score = models.PositiveIntegerField(null=True, default=5)

    # Estado
    status = models.BooleanField(default=True)

    # Fecha y hora
    date_time_create = models.DateTimeField(default=timezone.now)

    # Datos string
    def __str__(self):
        return self.title
