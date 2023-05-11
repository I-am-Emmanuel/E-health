from rest_framework import serializers
from . models import PatientModel, MedicalPersonnel, HospitalModel
from services.core.serializer import UserSerializer


class PatientModelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PatientModel

        fields = ['id', 'user_id', 'phone', 'profile_picture', 'gender', 'address',
                  'blood_group', 'genotype', 'medical_history']



class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalModel
        fields = '__all__'


class MedicalPersonelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = MedicalPersonnel
        fields = ['id', 'user_id', 'gender', 'hospital', 'specialty', 'hospital_staff_id', 'professional_license', 'profile_picture']
        # read_only_fields = ('id', 'created_at', 'updated_at')

    



