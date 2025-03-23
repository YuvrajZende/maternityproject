from django.urls import path
from .views import patient_register, patient_login, patient_dashboard

urlpatterns = [
    path('patients/register/', patient_register, name='patient_register'),
    path('patients/login/', patient_login, name='patient_login'),
    path('patients/dashboard/', patient_dashboard, name='patient_dashboard')
]
