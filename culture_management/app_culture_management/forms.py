from django import forms
from .models import Evento
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'entrada_gratuita': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'vagas': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("As senhas não coincidem.")