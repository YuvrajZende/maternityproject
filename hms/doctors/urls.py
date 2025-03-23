from django.urls import path
from .views import doctor_register, doctor_login,doctor_dashboard

urlpatterns = [
    path('doctor/register/', doctor_register, name='doctor_register'),
    path('doctor/login/', doctor_login, name='doctor_login'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard')
]
