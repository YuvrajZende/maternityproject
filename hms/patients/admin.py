from django.contrib import admin
from .models import Patient, MedicalRecord, Appointment

#admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
