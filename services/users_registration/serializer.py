from .models import User
from rest_framework import serializers
from . otpsender import sendOtp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

           
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        details = self.Meta.model(**validated_data)
        details.email = details.email
        # details.otp = details.otp(sendOtp(email=details.email))
        if password is not None:
            details.set_password(password)
        details.save()
        return details


class VerifyOtpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'otp']
        # email = serializers.EmailField()
        # otp = serializers.CharField(max_length = 6)



# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }


