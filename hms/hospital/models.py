from django.db import models
from authentication.models import CustomUser

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE ,related_name="patient_profile")
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Intern(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="intern_profile")
    mentor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="mentored_interns")

    def __str__(self):
        return f"Intern {self.user.username}"

'''
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment: {self.patient.user.username} with Dr. {self.doctor.user.username} on {self.date}"
'''