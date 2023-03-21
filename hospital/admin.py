from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(models.HospitalModel)
@admin.register(models.HospitalModel)
class HospitalAdmin(admin.ModelAdmin):
    search_fields = ['hospital_name']
    list_display = ['hospital_name', 'hospital_phone', 'address', 'doctor_first_name', 'doctors_phone', ]

