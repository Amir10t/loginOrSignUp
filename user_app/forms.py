from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    email.widget.attrs.update({'class': 'input-field'})

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    password.widget.attrs.update({'class': 'input-field'})

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    email.widget.attrs.update({'class': 'input-field'})

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    password.widget.attrs.update({'class': 'input-field'})

    repeat_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    repeat_password.widget.attrs.update({'class': 'input-field'})

class ResetPassword(forms.Form):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )