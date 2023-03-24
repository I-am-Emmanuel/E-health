from django.urls import path, include
from . import views

urlpatterns = [
    path('medical_personnel/', views.MedicalPersonnelView.as_view),
]
