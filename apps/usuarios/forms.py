from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control glyphicon glyphicon-user', 'maxlenght': 255,
                                               'placeholder': 'Nome de Usuário'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control glyphicon glyphicon-user', 'maxlenght': 255,
                                               'placeholder': 'Primeiro Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control glyphicon glyphicon-user', 'maxlenght': 255,
                                               'placeholder': 'Último Nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control has-feedback', 'type': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
        }
