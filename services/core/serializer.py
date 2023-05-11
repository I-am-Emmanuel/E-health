# from .models import User
# from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']

#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

           
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     details = self.Meta.model(**validated_data)
    #     details.email = details.email
    #     # details.otp = details.otp(sendOtp(email=details.email))
    #     if password is not None:
    #         details.set_password(password)
    #     details.save()
    #     return details


# class VerifyOtpUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['otp']
     


class UserCreateSerializer(BaseUserCreateSerializer):
    # first_name = serializers.CharField(unique=True)

    class Meta(BaseUserCreateSerializer.Meta):
        
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    # def create(self, validated_data):
    #     email = 


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', ]

