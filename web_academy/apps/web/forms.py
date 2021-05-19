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


class AcademyForm(forms.ModelForm):

    class Meta:
        model = AboutUs
        fields = ['company', 'name', 'name2', 'about_us', 'image', 'detail', 'phone', 'email', 'address',
                  'title_resume', 'resume']
        labels = {
            'company': 'Academia',
            'name': 'Titulo',
            'about_us': 'Descripcion',
            'name2': 'Titulo',
            'detail': 'Descripcion',
            'phone': 'Telefono',
            'email': 'Correo',
            'address': 'Direccion',
            'title_resume': 'Titulo',
            'resume': 'Descripcion',
        }
        widgets = {
            'company': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de la academia ...',
                    'id': 'company',
                    'class': 'form-control mb-3',
                }),
            'name': forms.TextInput(
                attrs={
                    'placeholder': '¿Quiénes somos? ...',
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
            'name2': forms.TextInput(
                attrs={
                    'placeholder': 'Nuestro Compromiso ...',
                    'id': 'name2',
                    'class': 'form-control mb-3',
                }),
            'title_resume': forms.TextInput(
                attrs={
                    'placeholder': 'Titulo de bienvenida ...',
                    'id': 'title_resume',
                    'class': 'form-control mb-3',
                }),
            'phone': forms.TextInput(
                attrs={
                    'id': 'phone',
                    'class': 'form-control mb-3',
                }),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Av. Italia 2010, Montevideo ...',
                    'id': 'address',
                    'class': 'form-control mb-3',
                }),
            'detail': forms.Textarea(
                attrs={
                    'id': 'detail',
                    'class': 'form-control mb-3',
                }),
            'about_us': forms.Textarea(
                attrs={
                    'id': 'about_us',
                    'class': 'form-control mb-3',
                }),
            'resume': forms.Textarea(
                attrs={
                    'id': 'resume',
                    'class': 'form-control mb-3',
                }),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'class': 'form-control mb-3',
                })
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'price', 'image', 'quantity_lesson', 'description', 'resume']
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'image': 'Imagen',
            'quantity_lesson': 'Cantidad de clases',
            'description': 'Descripcion',
            'resume': 'Resumen'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': '¿Quiénes somos? ...',
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control mb-3',
                }),
            'resume': forms.Textarea(
                attrs={
                    'id': 'resume',
                    'class': 'form-control mb-3',
                }),
        }
