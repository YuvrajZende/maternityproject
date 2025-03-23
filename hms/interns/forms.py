from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from hospital.models import CustomUser
from .models import Intern

class InternRegistrationForm(UserCreationForm):
    contact_number = forms.CharField(max_length=15)
    education = forms.CharField(max_length=255)
    specialization = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'contact_number', 'education', 'specialization']

class InternLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
