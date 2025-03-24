from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('dashboard')  # Change this to the appropriate URL
    else:
        form = UserRegisterForm()
    
    return render(request, 'authentication/register.html', {'form': form})


from .forms import LoginForm

def user_login(request):
    superusers = CustomUser.objects.filter(is_superuser=True)  # Fetch all superusers

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard/homepage
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form, 'superusers': superusers})

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
