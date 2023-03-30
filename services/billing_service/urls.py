from django.urls import path
from services.billing_service.views import WalletInfo, DepositFunds, VerifyDeposit

urlpatterns = [
    path('wallet_info/', WalletInfo.as_view()),
    path('payment/', DepositFunds.as_view()),
    path('payment/verify/<str:reference>/', VerifyDeposit.as_view()),
]































# from django.urls import path, include
# from rest_framework import routers
# from .views import BillingViewSet
# app_name = 'Billing'
#
# router = routers.DefaultRouter()
# # router.register(r'appointment', AppointmentViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('payment/', BillingViewSet.as_view(), name='payment'),
# ]
#
