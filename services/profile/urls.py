from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user/profile', views.PatientProfileViewSet)

urlpatterns = [
    path('',include(router.urls)),
   
]
