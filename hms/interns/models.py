from django.db import models
from authentication.models import CustomUser
from doctors.models import Intern
from hospital.models import Doctor
from patients.models import Patient

'''
class Intern(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'intern'}, related_name="intern_profile")
    supervisor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="supervised_interns")
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
'''

class AssignedPatient(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name="assigned_patients")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="assigned_interns")
    assigned_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.intern.user.username} - {self.patient.user.username}"
