from rest_framework import serializers

from . models import PatientModel


class PatientModelSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = PatientModel
        fields = ['id',  'phone', 'profile_picture', 'gender', 'address',
                 'blood_group', 'genotype', 'medical_history']

# class MedicalPersonnelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicalPersonnel
#         fields = ['first_name', 'last_name', '']
