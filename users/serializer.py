from rest_framework import serializers

from users.models import MedicalPersonnel


class MedicalPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPersonnel
        fields = ['first_name', 'last_name', '']