from django.contrib import admin
from services.appointment.models import BookingModel

# Register your models here.

@admin.register(BookingModel)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['medical_personnel', 'message', 'booked_status', 'appointment_day']
