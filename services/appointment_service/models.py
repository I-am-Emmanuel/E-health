from django.db import models
from django.contrib.auth import get_user_model
from services.profile.models import PatientModel, MedicalPersonnel
from services.hospital.models import HospitalModel
from uuid import uuid4


class AppointmentModel(models.Model):

    STATUS_CHOICES =[ 
        ('pending', 'PENDING'),
        ('cancled', 'CANCLED'),
        ('approved', 'APPROVED'),
    ]

    patient = models.ForeignKey(PatientModel, on_delete=models.PROTECT)
    # medical_personel = models.ForeignKey(MedicalPersonnel, on_delete=models.PROTECT, related_name='appointments_as_doctor')
    submit_time = models.DateTimeField(auto_now_add=True)
    meeting_date = models.DateField(null=False)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # status = models.BooleanField(default=False)


    # @admin.display(ordering='first__name')
    def first_name(self) -> str:
        return f'{self.patient.user.first_name}'
    
    def phone(self) -> str:
        return f'{self.patient.user.phone}'

    def __str__(self) -> str:
        return f'{self.submit_time} {self.patient.user.phone} {self.patient.user.medical_history}'


    class Meta:
        ordering = ['submit_time']
        permissions = [
            ('cancel_appointment', 'Can cancel appointment')
        ]
class AppointmentPageModel(models.Model):
    appointment = models.ForeignKey(AppointmentModel, on_delete=models.PROTECT, related_name='appoint')
    hospital = models.ForeignKey(HospitalModel, on_delete=models.PROTECT, related_name='hospital_detail')
    
class AppointmentCartModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

class AppointmentCartItemModel(models.Model):
    STATUS_CHOICES =[ 
        ('15 minutes', '15 minutes'),
        ('20 minutes', '20 minutes'),
        ('30 minutes', '30 minutes'),
    
    ]
    hospital = models.ForeignKey(MedicalPersonnel, on_delete=models.CASCADE)
    booked_time = models.CharField(max_length=20, choices=STATUS_CHOICES, default='15 minutes')
    # class Meta:
    #     unique_together = [['booking_cart', 'hospital']]

