from django import forms
from .models import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'rut_dgi', 'address', 'address2', 'city', 'postal_code',
                  'region', 'mobile', 'email']
        labels = {
            'name': "Name",
            'rut_dgi': "RUT DGI",
            'address': "Address",
            'address2': "Address2",
            'city': "City",
            'postal_code': "Postal code",
            'region': "Zone",
            'mobile': "Mobile",
            'email': "Email",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'address',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street addres line 2',
                    'id': 'address2',
                }),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'city',
                    'placeholder': 'City'
                }),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'region',
                    'placeholder': 'Zone'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code'
                }),
            'mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'mobile'
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email'
                }),
            'rut_dgi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'RUT',
                    'id': 'rut_dgi'
                }),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'nro_documento', 'logo', 'address', 'address2', 'city',
                  'postal_code', 'region', 'mobile', 'email', ]
        labels = {
            'name': "Name",
            'nro_documento': "Nro documento",
            'address': "Address",
            'address2': "Address2",
            'city': "City",
            'postal_code': "Postal code",
            'region': "Region",
            'mobile': "Mobile",
            'email': "Email",
            'logo': "Upload Image"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'street street-item',
                    'id': 'address',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'street street-item',
                    'placeholder': 'Street addres line 2',
                    'id': 'address2',
                }),
            'city': forms.TextInput(
                attrs={
                    'id': 'city',
                    'placeholder': 'City'
                }),
            'region': forms.TextInput(
                attrs={
                    'id': 'region',
                    'placeholder': 'Region'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code'
                }),
            'mobile': forms.TextInput(
                attrs={
                    'id': 'mobile'
                }),
            'nro_documento': forms.TextInput(
                attrs={
                    'id': 'nro_documento'
                }),
        }


class ActivityTypeForm(forms.ModelForm):
    class Meta:
        model = ActivityType
        fields = ['name', 'description']
        labels = {
            'name': "Name",
            'description': "Description"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                })
        }


class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = ['name', 'description']
        labels = {
            'name': "Name",
            'description': "Description"
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                    'class': 'form-control',
                    'rows': 4,
                    'cols': 15
                })
        }


class ServicesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(state=True)

    class Meta:
        model = Services
        fields = ['name', 'supplier']
        labels = {
            'name': 'Name',
            'supplier': 'Supplier'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control mb-3',
                }),
        }


class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ['name', 'code']
        labels = {
            'name': 'State',
            'code': 'Code'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control'
                }),
            'code': forms.TextInput(
                attrs={
                    'id': 'code',
                    'class': 'form-control'
                }),
        }


class CityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.filter(active=True)

    class Meta:
        model = City
        fields = ['name', 'state']
        labels = {
            'name': 'City',
            'state': 'State',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control'
                }),
        }
