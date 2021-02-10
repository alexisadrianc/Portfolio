from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from .models import *

CUSTOMER = '1'
EMPLOYEE = '2'
USER_TYPE = (
    (CUSTOMER, 'CUSTOMER'),
    (EMPLOYEE, 'EMPLOYEE'),
)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Username',
                    'name': 'username'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Password',
                    'name': 'pass'
                }),
        }


class RegisterUserForm(UserCreationForm):
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input--style-4',
            'id': 'password2',
        }
    ))

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'user_type']
        labels = {
            'username': 'User',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password': 'Password',
            'email': 'Email',
            'user_type': 'User type'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'username'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'last_name'
                }),
            'email': forms.TextInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input--style-4',
                    'name': 'password'
                }),

        }


class UsersForm(forms.ModelForm):
    """Adding new field password for validate password of the new user"""
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password2',
            'required': 'required',
            'placeholder': 'Confirm password',
        }
    ))

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'user_type']
        labels = {
            'username': 'User',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password': 'Password',
            'email': 'Email',
            'user_type': 'User type',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'username'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First name',
                    'id': 'first_name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last name',
                    'id': 'last_name'
                }),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'id': 'email'
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'name': 'password'
                }),
            'user_type': forms.Select(
                choices=USER_TYPE,
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def clean_password2(self):
        """ Validation pass method for validate password """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("The passwords are not equals ")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
