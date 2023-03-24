from rest_framework import serializers

from services.appointment_service.models import Appointment


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time', 'duration', 'message', 'status']
