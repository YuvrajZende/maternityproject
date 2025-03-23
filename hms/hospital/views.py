from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import HospitalRegistrationForm, HospitalLoginForm

def hospital_register(request):
    if request.method == 'POST':
        form = HospitalRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_dashboard')  # Redirect to login after registration
    else:
        form = HospitalRegistrationForm()
    return render(request, 'hospital/hospital_register.html', {'form': form})

def hospital_login(request):
    if request.method == 'POST':
        form = HospitalLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hospital_dashboard')  # Redirect after login
    else:
        form = HospitalLoginForm()
    return render(request, 'hospital/hospital_login.html', {'form': form})

def hospital_dashboard(request):
    return render(request , 'hospital/hospital_dashboard.html')