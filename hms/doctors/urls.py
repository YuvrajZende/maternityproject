from django.urls import path
from .views import doctor_dashboard, patient_list, intern_list

urlpatterns = [
    path('dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patients/', patient_list, name='patient_list'),
    path('interns/', intern_list, name='intern_list'),
]
