from rest_framework import serializers
from .models import Doctor, AssignedPatient, SupervisedIntern

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AssignedPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedPatient
        fields = '__all__'

class SupervisedInternSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisedIntern
        fields = '__all__'
