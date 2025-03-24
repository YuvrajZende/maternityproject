from django.urls import path
from .views import dashboard, doctor_list, patient_list, intern_list

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('patients/', patient_list, name='patient_list'),
    path('interns/', intern_list, name='intern_list'),
]
