from rest_framework import serializers
from . models import PatientModel, MedicalPersonnel, HospitalModel
from services.core.serializer import UserSerializer


class PatientModelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PatientModel

        fields = ['id', 'user_id', 'phone', 'profile_picture', 'gender', 'address',
                  'blood_group', 'genotype', 'medical_history']

class HospitalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalModel
        fields = ['id', 'name']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalModel
        fields = '__all__'


class MedicalPersonelSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    # hospital = serializers.PrimaryKeyRelatedField(queryset=HospitalModel.objects.all(), required=False, allow_null=True)

    class Meta:
        model = MedicalPersonnel
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

        extra_kwargs = {
            'hospital': {'required': False},
            'specialty': {'required': False},
            'hospital_staff_id': {'required': False},
            'professional_license': {'required': False},
            'profile_picture': {'required': False},
            'gender': {'required': False},
        }



# class MedicalPersonelSerializer(serializers.ModelSerializer):
#     hospital = serializers.PrimaryKeyRelatedField(queryset=HospitalModel.objects.all(), required=False, allow_null=True)

#     class Meta:
#         model = MedicalPersonnel
#         fields = '__all__'

#         read_only_fields = ('id', 'user', 'created_at', 'updated_at')

    # def create(self, validated_data):
    #     user_id = validated_data.pop('user', None)
    #     if user_id:
    #         validated_data['user_id'] = user_id
    #     return super().create(validated_data)
    



    # first_name = serializers.SerializerMethodField(method_name='user_first_name')
    # last_name = serializers.SerializerMethodField(method_name='user_last_name')

    # def user_first_name(self, users:PatientModel):
    #         return users.user.first_name

    # def user_last_name(self, users:PatientModel):
    #         return users.user.last_name

# class MedicalPersonnelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicalPersonnel
#         fields = ['first_name', 'last_name', '']
