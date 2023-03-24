from rest_framework import viewsets

from users.models import MedicalPersonnel
from users.serializer import MedicalPersonnelSerializer


# Create your views here.
class MedicalPersonnelView(viewsets.ModelViewSet):
    queryset = MedicalPersonnel.objects.all()
    serializer_class = MedicalPersonnelSerializer
