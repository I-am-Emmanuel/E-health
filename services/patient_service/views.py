from rest_framework import viewsets, generics
from .serializers import PatientSerializers
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
