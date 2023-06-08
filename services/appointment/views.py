from services.profile.models import PatientModel, MedicalPersonnel
from services.profile.user_permission import *
from services.core.models import User
from .models import BookingModel
from services.profile.user_permission import IsAdminOrReadOnly
#  AppointmentCartItemModel, AppointmentPageModel, AppointmentCartModel
from .serializers import BookingSerializers, MedicalPersonelListSerializer, MyBookingSerializers, DoctorsBookingDashboardSerializer as DBDS

from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend as DFB

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter as SF, OrderingFilter as OF
from rest_framework.decorators import action

# from datetime import datetime
from datetime import date
# AddCartItemSerializer,CreateAppointmentSerializer ,CartSerializer,AppointmentSerializers, AppointmentPageSerializers, AppointmentSerializers, CreateAppointmentSerializer, UpdateCartItemSerializer


class MedicalPersonelViewSet(ModelViewSet):
    queryset = MedicalPersonnel.objects.all()
    filter_backends = [SF, OF]
    search_fields = ['hospital']
    ordering_fields = ['id']
    serializer_class = MedicalPersonelListSerializer
    permission_classes = [IsAdminOrReadOnly]

    # @action(detail=True, permission_classes=[IsAdminOrReadOnly])
    def get_serializer_context(self):
        return {'request': self.request}


class BookingViewSet(ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializers
    filter_backends = [SF]
    search_fields = ['medical_personnel']
    http_method_names = ['post']
    # permission_classes = [IsAdminUser]
    
    # @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    # def get_queryset(self):
    #     if 
    def create(self, request):
        
        appointment_day = request.data.get('appointment_day')
        message = request.data.get('message')
        medical_personnel = request.data.get('medical_personnel')


        # Convert the date to a Python date object and check if the date field is empty
        try:
            appointment_date = date.fromisoformat(appointment_day)
        except ValueError:
            return Response({'error': 'Your date field is required'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the requested appointment date is in the future
        if appointment_date <= date.today():
            return Response({'error': 'Appointment date must be in the future'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            patient = PatientModel.objects.get(user_id=request.user.id)
        except PatientModel.DoesNotExist:
            return Response({'error': 'Make sure you have registered as a patient'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            medical_personnel = MedicalPersonnel.objects.get(id=medical_personnel)
        except MedicalPersonnel.DoesNotExist:
            return Response({'error': 'Medical personnel not found'}, status=status.HTTP_400_BAD_REQUEST)
        booking = BookingModel(
            patient=patient,
            medical_personnel=medical_personnel,
            appointment_day=appointment_date,
            message=message,
        )
        booking.save()
        serializer = BookingSerializers(booking)
       
        return Response({'Your booking has been created successfully. Wait patiently for your pending request!'}, status=status.HTTP_201_CREATED)


# from django.contrib.auth import get_user_model

class MyBookingViewSet(ModelViewSet):
    serializer_class = MyBookingSerializers
    # permission_classes = [IsAdminOrReadOnly]
    http_method_names = ['get', 'destroy']

    
    def get_queryset(self):
        
        patient = PatientModel.objects.filter(user__email=self.request.user.email).first()
        if not patient:
            return BookingModel.objects.none()
        return BookingModel.objects.filter(patient=patient)

    # @action(detail=False, permission_classes=[IsAuthenticated])
    def destroy(self, request, *args, **kwargs):
        patient = PatientModel.objects.filter(user__email=self.request.user.email).first()

        if BookingModel.objects.filter(patient=patient).exists():
            return super().destroy(request, *args, **kwargs)
        return Response({'error': "Booking cannot be deleted. You have no right to delete other people's order"}, status=status.HTTP_401_UNAUTHORIZED)
        
class DoctorsBookingDashboard(ModelViewSet):
    serializer_class = DBDS
    queryset = BookingModel
    # http_method_names = ['put', 'get']

    def get_queryset(self):
        doctor = MedicalPersonnel.objects.filter(user__email=self.request.user.email).first()
        if not doctor:
            return BookingModel.objects.none()
        return BookingModel.objects.filter(medical_personnel=doctor)

        if request.methods == perform_update:
            edited = BookingModel.objects.perform_update(serializer=DBDS)
            edited.save()       
        return BookingModel.objects.filter(medical_personnel=doctor)


    # def perform_update(self, serializer):
    #     doctor = MedicalPersonnel.objects.filter(user__email=self.request.user.email).first()
    #     if BookingModel.objects.filter(medical_personnel=doctor):
    #         edited = BookingModel.objects.perform_update(serializer=DBDS)
    #         edited.save()       
    #     return BookingModel.objects.filter(medical_personnel=doctor)