from rest_framework import viewsets, generics
from . serializers import AppointmentSerializers
from . models import Appointment


class AppointmentViewSet(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

