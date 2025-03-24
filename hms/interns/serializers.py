from rest_framework import serializers
from .models import Intern, AssignedPatient

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'

class AssignedPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedPatient
        fields = '__all__'
