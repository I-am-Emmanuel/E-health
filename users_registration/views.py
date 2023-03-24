# from django.shortcuts import render
from .models import User
from . serializer import UserSerializer, VerifyOtpUserSerializer

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

from django.contrib.auth import authenticate
from django.db.models import Q
from . otpsender import *



# Create your views here.

class SignUpViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        # password = data.get('password')

        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        sendOtp(serializer.data['email'])
        return Response({'message': f"Otp Successfully sent to {email}", 'data': serializer.data}, status=status.HTTP_200_OK)

        # return Response({'status': 'fail', 'message': 'You are not allowed to register'}, status=status.HTTP_406_NOT_ACCEPTABLE)

class VerifyOtpViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = VerifyOtpUserSerializer

    def post(self, request):
        data = request.data
        serializer = VerifyOtpUserSerializer(data=data)
        serializer.is_valid()
        email = serializer.data['email']
        otp = serializer.data['otp']

        user = User.objects.filter(email=email)
        if not user.exists():
            return Response({'message': 'something went wrong!',
             'data': 'invalid email'}, status=status.HTTP_404_NOT_FOUND)

        if not user[0].otp == otp:
            return Response({'message': 'wrong otp!', 
            'data': 'invalid otp token is provided'}, status=status.HTTP_404_NOT_FOUND)

        user = user.first() 
        user.is_verified = True
        user.save()
        return Response({'message': f"account verified correctly!"}, status=status.HTTP_200_OK)

class PatientSignUpViewclass(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        # password = data.get('password')

        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        sendOtp(serializer.data['email'])
        return Response({'message': f"Otp Successfully sent to {email}", 'data': serializer.data}, status=status.HTTP_200_OK)




