from rest_framework import viewsets, generics
from .serializers import DoctorSerializers
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers

#
# class DoctorCreateAPIView():
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializers
