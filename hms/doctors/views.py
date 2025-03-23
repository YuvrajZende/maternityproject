from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import DoctorRegistrationForm, DoctorLoginForm
from .models import Doctor

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_login')  # Redirect after registration
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctors/doctor_register.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('doctor_dashboard')  # Redirect to dashboard
    else:
        form = DoctorLoginForm()
    return render(request, 'doctors/doctor_login.html', {'form': form})


#@login_required
def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user) # Get the logged-in doctor

    context = {
        'doctor': doctor,
    }
    return render(request, 'doctors/doctor_dashboard.html', context)