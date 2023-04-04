from rest_framework import serializers

from services.appointment_service.models import AppointmentCartItemModel, AppointmentCartModel, AppointmentPageModel, AppointmentCartItemModel, AppointmentModel 
from services.profile.models import MedicalPersonnel, PatientModel




class SimpleMedicalStaffSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    # def new_name(self):
    #     return self.Meta.model.first_name +" "+ self.Meta.model.last_name
    
    def new_name(self, hospital_list:MedicalPersonnel):
        return self.hospital_list.first_name +" "+ self.hospital_list.last_name
    class Meta:
        model = MedicalPersonnel
        fields = ['id', 'hospital', 'name', 'specialty', 'profile_picture']
    
class CartItemSerializer(serializers.ModelSerializer):
    hospital = SimpleMedicalStaffSerializer()
    # hospital = MedicalPersonnel()
    class Meta:
        model = AppointmentCartItemModel
        fields = ['id', 'hospital']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    class Meta:
        model = AppointmentCartModel
        fields = ['id', 'items']

class AppointmentPageSerializers(serializers.ModelSerializer):
    hospital_detail = SimpleMedicalStaffSerializer(many=True)
    class Meta:
        model = AppointmentPageModel
        fields = ['id', 'hospital_detail']


class AppointmentSerializers(serializers.ModelSerializer):
    items = AppointmentPageSerializers()
    class Meta:
        model = AppointmentModel
        fields = ['id', 'patient', 'submit_time', 'meeting_date', 'message', 'items']


class AddCartItemSerializer(serializers.ModelSerializer):
    hospital_id = serializers.IntegerField()

    def validate_hospital_id(self, value):
        if not MedicalPersonnel.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No Medical Personnel with the given ID was found')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        hospital_id = self.validated_data['hospital_id']
        try:
            cart_item = AppointmentCartItemModel.objects.get(cart_id=cart_id, hospital_id=hospital_id)
            cart_item.save()
            self.instance = cart_item
        except AppointmentCartItemModel.DoesNotExist:
            self.instance = AppointmentCartItemModel.objects.create(cart_id=cart_id, **self.validated_data)
            return self.instance
    class Meta:
        model = AppointmentCartItemModel
        fields = ['id', 'hospital_id']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentCartItemModel

class CreateAppointmentSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_appointment_cart_id(self, cart_id):
        if not AppointmentCartModel.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart with the given ID was found')
        if AppointmentCartItemModel.objects.filter(cart_id= cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty.')
        return cart_id

    def save(self, **kwargs):
        with transaction.atomic():

            cart_id = self.validated_data['cart_id']
            patient = PatientModel.objects.get(user_id=self.context['user_id'])
            appointment = AppointmentModel.objects.create(patient=patient)

            cart_items = AppointmentCartItemModel.objects\
                        .select_related('hospital')\
                        .filter(cart_id=cart_id)
            appointment_items = [
                AppointmentPageModel(
                    appointment= appointment, 
                    hospital=item.hospital, 
                ) for item in cart_items
            ]
            AppointmentPageModel.objects.bulk_create(appointment_items)
            
            AppointmentCartModel.objects.filter(pk=cart_id).delete()

            order_created.send_robust(self.__class__, appointment=appointment)
            
            return order


    