from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import RegistroTrabajo


class RegistroTrabajoForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Cambia esto al formato que prefieras
            attrs={'type': 'date'}
        ),
        input_formats=['%Y-%m-%d'],  # Asegúrate de que este formato coincida con el anterior
    )

    class Meta:
        model = RegistroTrabajo
        fields = ['descripcion', 'horas_trabajadas', 'fecha', 'monto_pago']


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
