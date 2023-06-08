from django.urls import path, include
from rest_framework_nested import routers
from . import views

# app_name = 'Appointment'

router = routers.DefaultRouter()

router.register('patient/appointment', views.BookingViewSet, basename='appointment')
router.register('personnel/lists', views.MedicalPersonelViewSet, basename='medics')
router.register('bookings/history', views.MyBookingViewSet, basename='bookings')
router.register('doctor/dashboard', views.DoctorsBookingDashboard, basename='bookings')


# carts_router =  routers.NestedDefaultRouter(router, 'carts', lookup= 'cart')
# carts_router.register('items', views.AppointmentCartItemViewSet, basename='cart-items-detail')

urlpatterns = [
    path('', include(router.urls)),
    # path('appointment/', AppointmentViewSet.as_view(), name='doctor'),
    # other API URL patterns...
]
