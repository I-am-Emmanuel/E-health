from rest_framework import serializers

from services.doctor_service.models import Doctor


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'specialty', 'available_days']
