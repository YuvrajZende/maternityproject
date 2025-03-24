from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Intern
from patients.models import MedicalRecord, Appointment

@login_required
def dashboard(request):
    doctors = Doctor.objects.count()
    patients = Patient.objects.count()
    interns = Intern.objects.count()
    appointments = Appointment.objects.count()

    return render(request, 'hospital/dashboard.html', {
        'doctors': doctors,
        'patients': patients,
        'interns': interns,
        'appointments': appointments
    })

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

@login_required
def intern_list(request):
    interns = Intern.objects.all()
    return render(request, 'hospital/intern_list.html', {'interns': interns})
