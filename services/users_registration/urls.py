from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('signup', views.SignUpViewSet)
router.register('verify/otp', views.VerifyOtpViewSet)
# router.register('results', views.ElectionResultViewSet, basename='results')

urlpatterns = [
    path('', include(router.urls)),
]
