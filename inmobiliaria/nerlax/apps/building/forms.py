from django import forms
from .models import *


class buildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'address', 'address2', 'city', 'postal_code', 'supplier',
                  'region', 'unit_qty', 'amenities', 'type_resource', 'description']
        labels = {
            'name': 'Name',
            'address': 'Address',
            'unit_qty': 'Quantity of flat',
            'amenities': 'It has amenities ?',
            'type_resource': 'Property type',
            'supplier': 'Supplier',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Building name ...',
                    'id': 'name'
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'street street-item',
                    'placeholder': 'Street address'
                }),
            'address2': forms.TextInput(
                attrs={
                    'class': 'street street-item',
                    'placeholder': 'Street addres line 2'
                }),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'City'
                }),
            'region': forms.TextInput(
                attrs={
                    'placeholder': 'Zone'
                }),
            'postal_code': forms.TextInput(
                attrs={
                    'placeholder': 'Postal / zip code',
                    'id': 'postal_code'
                }),
            'amenities': forms.CheckboxInput(
                attrs={
                    'id': 'aminities'
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description',
                }),
            'supplier': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                })
        }


class unitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['number', 'meter_qty', 'flat', 'rent_price', 'renter',
                  'init_date', 'name', 'type_resource', 'building_id',
                  'renovation_date', 'expiration_date', 'description']
        labels = {
            'name': 'Name',
            'init_date': 'Contract start date',
            'number': 'Number of unit',
            'meter_qty': 'M2',
            'rent_price': 'Price of rent',
            'expiration_date': 'Contract expiration date',
            'renovation_date': 'Contract renovation date',
            'renter': 'Renter',
            'building_id': 'Building',
            'type_resource': 'Property type',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Unit name ...',
                    'id': 'name',
                    'class': 'street-item',
                }),
            'init_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'fas fa-calendar-alt',
                    'id': 'init_date'
                }),
            'number': forms.TextInput(
                attrs={
                    'placeholder': 'Unit ...',
                    'id': 'number'
                }),
            'flat': forms.TextInput(
                attrs={
                    'placeholder': 'Flat ...',
                    'id': 'flat'
                }),
            'meter_qty': forms.NumberInput(
                attrs={
                    'id': 'meter_qty'
                }),
            'rent_price': forms.NumberInput(
                attrs={
                    'id': 'rent_price'
                }),
            'expiration_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'fas fa-calendar-alt',
                    'id': 'expiration_date'
                }),
            'renovation_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'fas fa-calendar-alt',
                    'id': 'renovation_date'
                }),
            'description': forms.Textarea(
                attrs={
                    'id': 'description'
                }),

        }


class commonExpensesForm(forms.ModelForm):
    class Meta:
        model = CommonExpenses
        fields = ['building', 'payment_date', 'total_amount']
        labels = {
            'building': 'Building',
            'payment_date': 'Payment date',
            'total_amount': 'Amount',
        }
        widgets = {
            'payment_date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'placeholder': 'dd/mm/aaaa',
                    'class': 'street street-item',
                    'id': 'payment_date'
                }),
            'total_amount': forms.NumberInput(
                attrs={
                    'class': 'street street-item',
                    'id': 'total_amount'
                }
            )
        }


class commonExpensesLinesForm(forms.ModelForm):
    class Meta:
        model = CommonExpensesLines
        fields = ['concept', 'amount', 'common_expenses']
        labels = {
            'concept': 'Concept',
            'common_expenses': 'Concept expenses',
            'amount': 'Amount',
        }
        widgets = {
            'concept': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'concept'
                }),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'amount'
                }
            )
        }
