from django.urls import path
from . import views
from .views import hospital_register, hospital_login

urlpatterns = [
    path('hospital/register/', hospital_register, name='hospital_register'),
    path('hospital/login/', hospital_login, name='hospital_login'),
    path('hospital/dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
]