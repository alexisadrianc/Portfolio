from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('state',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Nombre ...'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Correo ...'
                }),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'subject',
                    'placeholder': 'Asunto'
                }),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Ingrese su mensaje ...',
                }),
        }


TEST = [
    ('1', 'Teórico'),
    ('2', 'Práctico')
]


class TestRequestForm(forms.ModelForm):
    class Meta:
        model = TestRequest
        fields = '__all__'
        exclude = ('state',)
        labels = {
            'name': 'Nombre completo',
            'test_type': 'Solicitud de Examen',
            'ci': 'Cédula',
            'trainer': 'Nombre del Instructor',
            'time_available': 'Disponibilidad horaria para el examen',
            'qty_lesson': 'Número de clases hechas',
            'phone': 'Número de Contacto',
            'email': 'E-mail'
        }

        widgets = {
            'test_type': forms.Select(
                choices=TEST,
                attrs={
                    'class': 'form-control',
                    'id': 'test_type'
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                }),
            'ci': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'ci',
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                }),
            'time_available': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'time_available',
                }),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'phone',
                }),
            'qty_lesson': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'qty_lesson',
                }),

        }
