from django.urls import path
from .views import patient_dashboard, appointment_history

urlpatterns = [
    path('dashboard/', patient_dashboard, name='patient_dashboard'),
    path('appointments/', appointment_history, name='appointment_history'),
]
