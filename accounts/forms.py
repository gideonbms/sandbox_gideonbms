from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import *



User = get_user_model()


class EmployeeRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(label='Email address', required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [

            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',

        ]

