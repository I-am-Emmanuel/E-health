from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(HospitalModel)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact_number']
    ordering = ['name']


@admin.register(HospitalStaff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staffs']
    ordering = ['staffs']

@admin.register(StaffDepartment)
class StaffDepartmentAdmin(admin.ModelAdmin):
    list_display = ['specialization']

