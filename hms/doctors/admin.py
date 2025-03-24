from django.contrib import admin
from .models import Doctor, AssignedPatient, SupervisedIntern

#admin.site.register(Doctor)
admin.site.register(AssignedPatient)
admin.site.register(SupervisedIntern)
