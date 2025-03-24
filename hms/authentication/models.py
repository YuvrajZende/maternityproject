from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('intern', 'Intern'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
