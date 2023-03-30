from django.db import models

# Create your models here.

class HospitalModel(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=250, unique=True, blank=False)
    contact_number = models.CharField(max_length=11, unique=True)
    

    def __str__(self) -> str:
        return self.name

class HospitalStaff(models.Model):
    staffs = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.staffs

class StaffDepartment(models.Model):
    specialization = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return self.specialization