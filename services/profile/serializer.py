from rest_framework import serializers
from . models import PatientModel, MedicalPersonnel


class PatientModelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = PatientModel
    
        fields = ['id', 'user_id', 'phone', 'profile_picture', 'gender', 'address',
                 'blood_group', 'genotype', 'medical_history']



class MedicalPersonelSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = MedicalPersonnel
    
        fields = ['id', 'user_id', 'profile_picture', 'hospital', 'hospital_staff_id', 'specialty', 'medical_profession', 'gender']




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
