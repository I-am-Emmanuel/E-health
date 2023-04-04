from . models import MedicalPersonnel, PatientModel
from . serializer import PatientModelSerializer, MedicalPersonelSerializer
from services.hospital.models import HospitalModel
from . user_permission import *

from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientModel.objects.all()
    serializer_class = PatientModelSerializer
    # permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewPatientHistoryPermission])
    def history(self, request, pk):
        return Response('ok')


    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    @action(detail=False, methods= ['GET', 'PUT'],  permission_classes=[IsAuthenticated])
    def me(self, request):
        (patient, created) = PatientModel.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':

        # request.user # This wil be sent to Anonymous User Class
            serializer = PatientModelSerializer(patient)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PatientModelSerializer(patient, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'profile updated successfully', 'data': serializer.data})


class MedicalPersonelProfileViewSet(ModelViewSet):
    queryset = MedicalPersonnel.objects.all()
    serializer_class = MedicalPersonelSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewPatientHistoryPermission])
    def history(self, request, pk):
        return Response('ok')


    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    @action(detail=False, methods= ['GET', 'PUT'],  permission_classes=[IsAuthenticated])
    def me(self, request):
        (medical_personel, created) = MedicalPersonnel.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':

        # request.user # This wil be sent to Anonymous User Class
            serializer = MedicalPersonelSerializer(medical_personel)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = MedicalPersonelSerializer(medical_personel, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'profile updated successfully', 'data': serializer.data})

    

# class MedicalPersonnelView(viewsets.ModelViewSet):
#     queryset = MedicalPersonnel.objects.all()
#     serializer_class = MedicalPersonnelSerializer
