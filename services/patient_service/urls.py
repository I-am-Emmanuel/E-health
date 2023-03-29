from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet

app_name = 'Patient'

router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # other API URL patterns...
]
