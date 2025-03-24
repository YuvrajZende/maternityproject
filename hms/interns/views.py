from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Intern, AssignedPatient

@login_required
def intern_dashboard(request):
    intern = get_object_or_404(Intern, user=request.user)
    assigned_patients = AssignedPatient.objects.filter(intern=intern)

    return render(request, 'interns/intern_dashboard.html', {
        'intern': intern,
        'assigned_patients': assigned_patients
    })

@login_required
def assigned_patients(request):
    intern = get_object_or_404(Intern, user=request.user)
    assigned_patients = AssignedPatient.objects.filter(intern=intern)

    return render(request, 'interns/assigned_patients.html', {'assigned_patients': assigned_patients})
