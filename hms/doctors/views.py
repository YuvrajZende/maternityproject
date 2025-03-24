from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor, AssignedPatient, SupervisedIntern

@login_required
def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    assigned_patients = AssignedPatient.objects.filter(doctor=doctor)
    supervised_interns = SupervisedIntern.objects.filter(doctor=doctor)

    return render(request, 'doctors/doctor_dashboard.html', {
        'doctor': doctor,
        'assigned_patients': assigned_patients,
        'supervised_interns': supervised_interns
    })

@login_required
def patient_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    assigned_patients = AssignedPatient.objects.filter(doctor=doctor)

    return render(request, 'doctors/patient_list.html', {'assigned_patients': assigned_patients})

@login_required
def intern_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    supervised_interns = SupervisedIntern.objects.filter(doctor=doctor)

    return render(request, 'doctors/intern_list.html', {'supervised_interns': supervised_interns})
