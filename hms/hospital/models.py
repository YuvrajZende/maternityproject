from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('hospital', 'Hospital'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('intern', 'Intern'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    # Fix the error by adding related_name to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

class Hospital(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
