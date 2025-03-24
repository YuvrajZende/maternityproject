from django.db import models
from authentication.models import CustomUser
from hospital.models import Doctor, Patient

'''
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'}, related_name="patient_profile")
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
'''

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    record_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record: {self.patient.user.username} - {self.record_date}"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patients_appointments")
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment: {self.patient.user.username} with Dr. {self.doctor.user.username} on {self.date}"
