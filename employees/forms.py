from django.forms import ModelForm, Textarea, TextInput, Select
from django.utils.translation import gettext_lazy as _
from .models import Employee
from .styles import Style


# SECTION - Form empleado
class EmployeesForm(ModelForm):
    # Constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Atributos
        self.fields["name"].widget.attrs["class"] = Style.ClassStyle.get_default_input()

    # Relación
    class Meta:
        # Modelo
        model = Employee
        # Columnas a mostrar
        fields = [
            "name",
            "phone",
            "gender",
        ]  # Fields a mostrar
        # fields = "__all__" # Todas las fields
        # exclude = ["amount",] # Fields a ocultar

        # Características del form
        widgets = {
            "name": TextInput(attrs={"placeholder": "Edain Jesus"}),
            "phone": TextInput(
                attrs={"class": Style.ClassStyle.get_default_input(), "type": "number"}
            ),
            "gender": Select(attrs={"class": Style.ClassStyle.get_select_input()}),
        }

        # Etiquetas
        labels = {
            "name": _("Nombre completo"),
            "phone": _("Teléfono personal"),
            "gender": _("Genero"),
        }
        # Textos de ayuda
        help_texts = {
            "phone": _("Solo números y máximo 10 dígitos."),
        }
        # Textos de errores
        error_messages = {
            "name": {"unique": _("El nombre ya esta en uso")},
            "phone": {
                "max_length": _("El teléfono es demacrado largo."),
            },
        }
