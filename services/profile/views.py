from . models import MedicalPersonnel, PatientModel, HospitalModel
from . serializer import PatientModelSerializer, MedicalPersonelSerializer
from . user_permission import *

from rest_framework import status
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class PatientProfileViewSet(ModelViewSet):
    queryset = PatientModel.objects.all()
    serializer_class = PatientModelSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewPatientHistoryPermission])
    def history(self, request, pk):
        return Response('ok')

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




# class MedicalPersonelProfileViewSet(ModelViewSet):
#     queryset = MedicalPersonnel.objects.all()
#     serializer_class = MedicalPersonelSerializer
#     permission_classes = [IsAuthenticated]
#     # lookup_field = 'user__username'

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             user = request.user.id
#             try:
#                 medical_personnel = MedicalPersonnel.objects.get_or_create(user_id=user)
#                 serializer = self.serializer_class(medical_personnel)
#                 return Response(serializer.data)
#             except MedicalPersonnel.DoesNotExist:
#                 return Response({'error': 'Medical personnel not found.'}, status=status.HTTP_404_NOT_FOUND)

#         elif request.method == 'PUT':
#             instance = self.get_object()
#             if instance is None:
#                 return Response({'error': 'Medical personnel not found.'}, status=status.HTTP_404_NOT_FOUND)

#             serializer = self.serializer_class(instance, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)

# class MedicalPersonelProfileViewSet(ModelViewSet):
#     queryset = MedicalPersonnel.objects.all()
#     serializer_class = MedicalPersonelSerializer
#     permission_classes = [IsAdminUser]

#     @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         (medical_personel, created) = MedicalPersonnel.objects.get_or_create(user_id=request.user.id)
#         if request.method == 'GET':
#             serializer = MedicalPersonelSerializer(medical_personel)
#             return Response(serializer.data)

#         elif request.method == 'PUT':
#             data = request.data
#             if not medical_personel.user_profile:
#                 # create a new user_profile if it does not exist
#                 medical_personel.user_profile = UserProfile.objects.create()
#             serializer = MedicalPersonelSerializer(medical_personel, data=data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'message': 'Profile updated successfully.', 'data': serializer.data})

class MedicalPersonelProfileViewSet(ModelViewSet):
    queryset = MedicalPersonnel.objects.all()
    serializer_class = MedicalPersonelSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'user__username'

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        if request.method == 'GET':
            user = request.user.id
            try:
                medical_personnel = MedicalPersonnel.objects.get(user_id=user)
                serializer = self.serializer_class(medical_personnel)
                return Response(serializer.data)
            except MedicalPersonnel.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        elif request.method == 'PUT':
            if not request.user.is_authenticated:
                return Response({'error': 'User is not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)

            data = request.data.copy()
            data['user'] = request.user.id
            
            try:
                medical_personnel = MedicalPersonnel.objects.get(user=request.user)
                data['hospital_id'] = medical_personnel.hospital_id
                serializer = self.serializer_class(medical_personnel, data=data)
            except MedicalPersonnel.DoesNotExist:
                serializer = self.serializer_class(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
