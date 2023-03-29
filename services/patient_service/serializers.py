from rest_framework import serializers

from services.patient_service.models import Patient


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender']
