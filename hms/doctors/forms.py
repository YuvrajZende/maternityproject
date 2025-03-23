from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Doctor, Hospital

class DoctorRegistrationForm(UserCreationForm):
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(), label="Hospital")
    specialization = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)
    license_number = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'doctor'
        if commit:
            user.save()
            Doctor.objects.create(
                user=user,
                hospital=self.cleaned_data['hospital'],
                specialization=self.cleaned_data['specialization'],
                contact_number=self.cleaned_data['contact_number'],
                license_number=self.cleaned_data['license_number']
            )
        return user

class DoctorLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)
