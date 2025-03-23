from django.db import models
from hospital.models import CustomUser, Hospital 
from doctors.models import Doctor

class Intern(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="interns")
    supervising_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="interns")
    contact_number = models.CharField(max_length=15, unique=True)
    education = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    training_status = models.CharField(max_length=50, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"