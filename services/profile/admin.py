from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.PatientModel)

@admin.register(models.PatientModel)
class PatientModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'blood_group', 'genotype', 'phone' ]
    ordering = ['user__first_name', 'user__last_name']
    list_select_related = ['user']
    search_fields= ['first_name__istartswith', 'last_name__istartswith']
    # autocomplete_fields = ['user']


@admin.register(models.MedicalPersonnel)
class MedicalPersonelModelAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                     'last_name', 'specialty', 'gender', ]
    ordering = ['user__first_name', 'user__last_name', 'specialty']
    list_select_related = ['user']
    search_fields= ['hospital']

@admin.register(models.HospitalModel)
class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact']

