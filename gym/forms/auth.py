from django import forms
from django.contrib.auth.forms import UserCreationForm

from gym.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'fullname']
