from . models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        details = self.Meta.model(**validated_data)
        details.email = details.email
        if password is not None:
            details.set_password(password)
        details.save()
        return details


        