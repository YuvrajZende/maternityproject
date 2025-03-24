from django.db import models
from authentication.models import CustomUser
from hospital.models import Doctor, Patient, Intern
'''
from patients.models import Patient
from interns.models import Intern

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return f"Dr. {self.user.username}"
'''

class AssignedPatient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="assigned_patients")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="assigned_doctors")
    assigned_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor.user.username} - {self.patient.user.username}"

class SupervisedIntern(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="supervised_interns")
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name="supervising_doctor")

    def __str__(self):
        return f"Dr. {self.doctor.user.username} supervises {self.intern.user.username}"
