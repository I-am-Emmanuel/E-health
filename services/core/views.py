# # from django.shortcuts import render
# from .models import User
# from . serializer import UserSerializer, VerifyOtpUserSerializer

# from rest_framework.response import Response
# from rest_framework import status, generics
# from rest_framework.viewsets import ModelViewSet, GenericViewSet
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

# from django.contrib.auth import authenticate
# from django.db.models import Q
# from . otpsender import *



# # Create your views here.

# class SignUpViewSet(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def post(self, request):
#         data = request.data
#         email = data.get('email')
#         # password = data.get('password')

        
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         sendOtp(serializer.data['email'])
#         return Response({'message': f"Otp Successfully sent to {email}", 'data': serializer.data}, status=status.HTTP_200_OK)

#         # return Response({'status': 'fail', 'message': 'You are not allowed to register'}, status=status.HTTP_406_NOT_ACCEPTABLE)
# # class LoginView(generics.GenericAPIView):
# #     serializer_class = UserSerializer
# #     queryset = User.objects.all()

# #     def post(self, request):
# #         data = request.data
# #         email = data.get('email')
# #         password= data.get('password')      
        

# #         user = authenticate(email=email, password=password)

# #         if user is None:
# #             return Response({"status": "Fail", "message": "This field need a correct data!! Make sure you input your registerd data correctly!!!"}, status=status.HTTP_400_BAD_REQUEST)

# #         if not user.check_password(password):
# #             return Response({'status': 'Fail', 'message': 'Incorrect details!!'}, status=status.HTTP_400_BAD_REQUEST)
        
# #         serializer = self.serializer_class(user)
    
# #         return Response({"status": 'Login successful', 'user': serializer.data })

# class VerifyOtpViewSet(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = VerifyOtpUserSerializer

#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid()
#         # email = serializer.data['email']
#         otp = serializer.data['otp']

#         user = User.objects.filter(otp=otp)
#         if not user.exists():
#             return Response({'message': 'something went wrong!',
#              'data': 'invalid email'}, status=status.HTTP_404_NOT_FOUND)

#         if not user[0].otp == otp:
#             return Response({'message': 'wrong otp!', 
#             'data': 'invalid otp token is provided'}, status=status.HTTP_404_NOT_FOUND)

#         user = user.first() 
#         user.is_verified = True
#         user.save()
#         return Response({'message': f"account verified correctly!"}, status=status.HTTP_200_OK)






