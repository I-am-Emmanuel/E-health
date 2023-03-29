from django.urls import path, include
from rest_framework import routers
from .views import DoctorViewSet

app_name = 'Doctor'

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # other API URL patterns...
]
