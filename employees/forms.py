from django.forms import ModelForm
from .models import Employee

#SECTION - Form empleado
class EmployeesForm(ModelForm):
    
    # Relación
    class Meta:
        # Modelo
        model = Employee
        # Columnas a mostrar
        fields = ['name', 'phone', 'gender']
        # fields = '__all__'  # Todas las fields