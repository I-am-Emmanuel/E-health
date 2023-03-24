from rest_framework import viewsets
from rest_framework.response import Response
from . models import MedicalPersonnel, PatientModel
from . serializer import PatientModelSerializer
from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientModel.objects.all()
    serializer_class = PatientModelSerializer

    def post(self, request):
        # data = request.data
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'messsage': 'profile updated successfully'}, status=status.HTTP_200_OK)
        serializer.save()
        return Response({'message': 'profile needed to be completed before using the platform'}, status=status.HTTP_200_OK)

    

# class MedicalPersonnelView(viewsets.ModelViewSet):
#     queryset = MedicalPersonnel.objects.all()
#     serializer_class = MedicalPersonnelSerializer
