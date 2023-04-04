from django.contrib import admin
from services.appointment_service.models import AppointmentModel

# Register your models here.

@admin.register(AppointmentModel)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['submit_time', 'first_name', 'status', 'message', 'status', 'meeting_date' ]
