from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Patient
from .forms import PatientRegistrationForm, PatientLoginForm

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('patient_dashboard')  # Redirect to a dashboard or home page
    else:
        form = PatientRegistrationForm()
    return render(request, 'patients/patient_registration.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_dashboard')  # Redirect to a dashboard or home page
    else:
        form = PatientLoginForm()
    return render(request, 'patients/patient_login.html', {'form': form})



@login_required
def patient_dashboard(request):
    return render(request, 'patients/patient_dashboard.html')