from rest_framework import viewsets

from profile.models import MedicalPersonnel
from profile.serializer import MedicalPersonnelSerializer


# Create your views here.
class MedicalPersonnelView(viewsets.ModelViewSet):
    queryset = MedicalPersonnel.objects.all()
    serializer_class = MedicalPersonnelSerializer
