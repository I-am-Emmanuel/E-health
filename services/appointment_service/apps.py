from django.apps import AppConfig

from services import appointment_service


#
# class AppointmentServiceConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'appointment_service'
#
# from django.apps import AppConfig

class AppointmentServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services.appointment_service'
