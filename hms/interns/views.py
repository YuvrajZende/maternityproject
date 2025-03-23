from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import InternRegistrationForm, InternLoginForm
from hospital.models import CustomUser
from .models import Intern

def intern_register(request):
    if request.method == 'POST':
        form = InternRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Intern.objects.create(
                user=user,
                contact_number=form.cleaned_data['contact_number'],
                education=form.cleaned_data['education'],
                specialization=form.cleaned_data['specialization']
            )
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or homepage
    else:
        form = InternRegistrationForm()
    
    return render(request, 'intern_register.html', {'form': form})

def intern_login(request):
    if request.method == 'POST':
        form = InternLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or homepage
    else:
        form = InternLoginForm()
    
    return render(request, 'intern_login.html', {'form': form})

def intern_logout(request):
    logout(request)
    return redirect('intern_login')
