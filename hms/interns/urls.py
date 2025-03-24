from django.urls import path
from .views import intern_dashboard, assigned_patients

urlpatterns = [
    path('dashboard/', intern_dashboard, name='intern_dashboard'),
    path('assigned-patients/', assigned_patients, name='assigned_patients'),
]
