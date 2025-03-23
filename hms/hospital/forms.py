from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Hospital

class HospitalRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    address = forms.CharField(widget=forms.Textarea)
    contact_number = forms.CharField(max_length=15)
    registration_number = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'hospital'
        if commit:
            user.save()
            Hospital.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                address=self.cleaned_data['address'],
                contact_number=self.cleaned_data['contact_number'],
                registration_number=self.cleaned_data['registration_number']
            )
        return user

class HospitalLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


