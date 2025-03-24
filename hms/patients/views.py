from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, MedicalRecord, Appointment

@login_required
def patient_dashboard(request):
    patient = get_object_or_404(Patient, user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    medical_records = MedicalRecord.objects.filter(patient=patient)

    return render(request, 'patients/patient_dashboard.html', {
        'patient': patient,
        'appointments': appointments,
        'medical_records': medical_records
    })

@login_required
def appointment_history(request):
    patient = get_object_or_404(Patient, user=request.user)
    appointments = Appointment.objects.filter(patient=patient)

    return render(request, 'patients/appointment_history.html', {'appointments': appointments})

