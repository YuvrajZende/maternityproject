from django.contrib import admin
from .models import Doctor, Patient, Intern

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Intern)
#admin.site.register(Appointment)
