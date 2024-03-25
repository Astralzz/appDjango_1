import random
from django.db import models
from django.utils import timezone


# SECTION - Position de empleado
class PositionEmployee(models.Model):
    # Nombre
    name = models.CharField(max_length=120, unique=True)
    # Salario
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Descripción
    description = models.TextField(max_length=1000, null=True)
    # Fecha y hora de creación
    date_time_create = models.DateTimeField(auto_now_add=True)
    # Fecha y hora de ultima edición
    date_time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# SECTION - Pago recibido
class PaymentsReceived(models.Model):
    # Cargo
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Fecha
    date = models.DateField(default=timezone.now)
    # Hora
    hour = models.TimeField(default=timezone.now)
    # Fecha y hora de creación
    date_time_create = models.DateTimeField(auto_now_add=True)
    # Fecha y hora de ultima edición
    date_time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)


# SECTION - Empleado
class Employee(models.Model):
    # Géneros
    GENDER_CHOICES = [("F", "FEMENINO"), ("M", "MASCULINO"), ("N", "SIN ESPECIFICAR")]

    # No de empleado
    noEmployee = models.CharField(max_length=8, unique=True, db_index=True)
    # Nombre
    name = models.CharField(max_length=120, unique=True)
    # Teléfono
    phone = models.CharField(max_length=10, null=True)
    # Genero
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")
    # Esta activo
    active = models.BooleanField(default=True)
    # Pagos recibidos
    payments = models.ManyToManyField(PaymentsReceived, related_name="payments")
    # Fecha y hora de creación
    date_time_create = models.DateTimeField(auto_now_add=True)
    # Fecha y hora de ultima edición
    date_time_update = models.DateTimeField(auto_now=True)

    # Al guardar
    def save(self, *args, **kwargs):
        # ? No existe no de empleado
        if not self.noEmployee:
            # Generamos numero
            self.generate_unique_employee_number()

        # Llama al método save() del modelo padre para guardar el objeto
        super().save(*args, **kwargs)

    # Generar no de empleado
    def generate_unique_employee_number(self):
        # Genera un número de empleado único de 8 dígitos
        self.noEmployee = "".join(str(random.randint(0, 9)) for _ in range(8))
        # Verifica que el número generado no exista ya en la base de datos
        while Employee.objects.filter(noEmployee=self.noEmployee).exists():
            self.noEmployee = "".join(str(random.randint(0, 9)) for _ in range(8))

    def __str__(self):
        return self.name
