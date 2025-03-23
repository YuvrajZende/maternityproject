from django.db import models
from hospital.models import CustomUser, Hospital

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialization}"
