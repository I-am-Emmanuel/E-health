from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()

router.register('profile', views.PatientProfileViewSet, basename='profile')
router.register('medical_personel', views.MedicalPersonelProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(router.urls)),
   
]
