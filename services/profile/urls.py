# from django.urls import path, include
# from . import views
# # from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

# from rest_framework.routers import DefaultRouter

# # router = DefaultRouter()
# # router.register(r'me', views.MedicalPersonelProfileViewSet, basename='medical_personel')

# # urlpatterns = [
# #     # ...
# #     # path('user/medical_personel/', include(router.urls)),
# #     path('user/medical_personel/<int:pk>/', include(router.urls)),  # add the 'pk' parameter
# #     # ...
# # ]



# router = routers.DefaultRouter()

# router.register('profile', views.PatientProfileViewSet, basename='profile')
# router.register('medical_personel', views.MedicalPersonelProfileViewSet, basename='medical')

# urlpatterns = [
#     path('', include(router.urls)),
    
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services.profile.views import PatientProfileViewSet, MedicalPersonelProfileViewSet

router = DefaultRouter()
router.register('profile', PatientProfileViewSet, basename='profile')
router.register('medical_personel', MedicalPersonelProfileViewSet, basename='medical_personel')

urlpatterns = [
    path('', include(router.urls)),
    path('medical_personel/me/', MedicalPersonelProfileViewSet.as_view({'get': 'me', 'put': 'update'}), name='medical_personel_profile'),
]

