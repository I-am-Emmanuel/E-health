from rest_framework import viewsets
from . serializers import AppointmentSerializers
from . models import Appointment


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

