# from django.shortcuts import render
from .models import Register
from . serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from django.db.models import Q
from hospital.models import HospitalModel


# Create your views here.

class DoctorSignUpView(generics.GenericAPIView):
    queryset = Register
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if HospitalModel.objects.filter(doctors_email=email):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'status': 'Successfully signup'}, status=status.HTTP_201_CREATED)

        return Response({'status': 'fail', 'message': 'You are not allowed to register'}, status=status.HTTP_406_NOT_ACCEPTABLE)








