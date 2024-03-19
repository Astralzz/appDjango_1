from django import forms
from django.core.validators import RegexValidator
from .models import TeacherCategory
import re


# Validator
phone_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="El número de teléfono debe tener exactamente 10 dígitos.",
)


# Formulario de maestro
class TeacherForm(forms.Form):
    # Nombre
    name = forms.CharField(
        label="Nombre",
        required=True,
        max_length=120,
        min_length=2,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )

    # Email
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )

    # Categorías de maestros
    category = forms.ModelChoiceField(
        label="Categoría",
        queryset=TeacherCategory.objects.all(),
        empty_label="Selecciona una categoría",
        required=True,
        widget=forms.Select(attrs={"class": "form-control mb-3"}),
    )

    # Teléfono
    phone = forms.CharField(
        label="Teléfono",
        required=True,
        max_length=10,
        min_length=10,
        validators=[phone_validator],
        help_text="Obligatorio 10 caracteres",
        widget=forms.NumberInput(attrs={"class": "form-control mb-3"}),
    )

    # Dirección
    direction = forms.CharField(
        label="Dirección",
        required=False,
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control mb-3"}),
    )

    # Validación extra de email
    def clean_email(self):
        # Email
        email = self.cleaned_data.get("email")

        # ? es valido
        if not re.match(r"^(\d{8})@uagro\.mx$", email):
            raise forms.ValidationError(
                "El correo electrónico debe comenzar con 8 dígitos numéricos seguidos de '@uagro.mx', ejemplo (15240863@uagro.mx)."
            )

        return email
