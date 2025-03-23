from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Patient
from .models import CustomUser  # Assuming CustomUser is your user model

class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                               widget=forms.Select(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    medical_history = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)

    class Meta:
        model = CustomUser  # Assuming your user model handles authentication
        fields = ['username', 'email', 'password1', 'password2', 'age', 'gender', 'contact_number', 'medical_history']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class PatientLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
