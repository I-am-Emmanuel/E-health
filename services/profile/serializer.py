from rest_framework import serializers
from . models import PatientModel, MedicalPersonnel
from .models import PatientModel
from services.hospital.models import HospitalModel


class PatientModelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PatientModel

        fields = ['id', 'user_id', 'phone', 'profile_picture', 'gender', 'address',
                  'blood_group', 'genotype', 'medical_history']

class HospitalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalModel
        fields = ['name']


class MedicalPersonelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = MedicalPersonnel
    
        fields = ['id', 'user_id', 'profile_picture', 'hospital_staff_id', "professional_license", 'specialty', 'medical_profession', 'gender', 'hospital']

    # def get_hospital(query:HospitalModel):
    #         return query.



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
