from django.db import models

# Create your models here.


class HospitalModel(models.Model):
    hospital_name = models.CharField(max_length=250, null=False, unique=True)
    address = models.CharField(max_length=255)
    #  = models.EmailField(null=True)
    hospital_phone = models.CharField(null=False, max_length= 14)
    doctor_first_name = models.CharField(max_length=250, null=False)
    doctor_last_name = models.CharField(max_length=250, null=False)
    doctors_email = models.EmailField(unique=True)
    doctors_phone = models.CharField(unique=True, max_length= 14)

    def __str__(self):
        self.hospital_name








