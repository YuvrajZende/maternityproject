from django.urls import path
from .views import intern_register, intern_login, intern_logout

urlpatterns = [
    path('intern/register/', intern_register, name='intern_register'),
    path('intern/login/', intern_login, name='intern_login'),
    path('intern/logout/', intern_logout, name='intern_logout'),
]
