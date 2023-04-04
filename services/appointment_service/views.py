from services.profile.models import PatientModel

from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

from services.profile.user_permission import *
from .models import AppointmentModel, AppointmentCartItemModel, AppointmentPageModel, AppointmentCartModel
from .serializers import AddCartItemSerializer,CreateAppointmentSerializer ,CartSerializer,AppointmentSerializers, AppointmentPageSerializers, AppointmentSerializers, CreateAppointmentSerializer, UpdateCartItemSerializer


class AppointmentCartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = AppointmentCartModel.objects.prefetch_related('items__hospital').all()
    serializer_class = CartSerializer
    # AppointmentSerializers

class AppointmentCartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer

        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer 
        return CartItemSerializer
         
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return AppointmentCartItemModel.objects.filter(cart_id=self.kwargs['cart_pk'])\
                                .select_related('product')


class AppointmentViewSet(ModelViewSet):

    # queryset = AppointmentModel.objects.all()
    # serializer_class = AppointmentSerializers
    # permision_classes = [IsAuthenticated]

    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateAppointmentSerializer(data=request.data, context={'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        appointment = serializer.save()
        serializer = AppointmentSerializers(appointment)
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAppointmentSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return AppointmentSerializers

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return AppointmentModel.objects.all()

        patient_id = PatientModel.objects.only(
            'id').get(user_id=user_id)
        return AppointmentModel.objects.filter(patient_id=patient_id)


