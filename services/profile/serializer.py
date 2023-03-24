from rest_framework import serializers

from . models import PatientModel


class PatientModelSerializer(serializers.Serializer):
    class Meta:
        model = PatientModel
        fields = ['user__first_name', 'user__last_name', 'phone', 'profile_picture', 'gender', 'address',
                 'blood_group', 'genotype', 'medical_history']

# class MedicalPersonnelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicalPersonnel
#         fields = ['first_name', 'last_name', '']