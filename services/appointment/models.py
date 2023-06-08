from django.db import models
from django.contrib.auth import get_user_model
from services.profile.models import PatientModel, MedicalPersonnel, HospitalModel
from uuid import uuid4


# class Cart(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     created_at = models.DateTimeField(auto_now_add=True)
class BookingModel(models.Model):

    STATUS_CHOICES =[ 
        ('pending', 'PENDING'),
        ('canceled', 'CANCELED'),
        ('approved', 'APPROVED'),
    ]
    SPECIALTY_CHOICES = (

        ('General doctor', 'General Doctor'),
        ('Epidemiologist', 'Epidemiologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Dentist', 'Dentist'),
        ('Surgeon', 'Surgeon'),
        ('Dermatologist', 'Dermatologist'),
        ('Plastic surgeon', ' Plastic Surgeon'),
        ('Psychiatrist', 'Psychiatrist'),
    )

    HOSPITAL_CHOICES = (
        ('Harvey Hospital (Yaba, Lagos)', 'Harvey State Hospital Yaba'),
        ('U.C.H (Gate, Ibadan)', 'University College Hospital Ibadan'),
        ('LUTH (Onipanu, Lagos)', 'Lagos State University Teaching Hospital'),
        ('Oluyoro (Oluyoro Agugu, Ibadan)', 'Oluyoro Catholic Hospital'),
        ('UITH (Eleko Road Ilorin)', 'University of Ilorin College Hospital'),
    )
    
    medical_personnel = models.ForeignKey(MedicalPersonnel, on_delete=models.CASCADE)
    appointment_day = models.DateField(blank=False)
    booked_status = models.CharField(choices=STATUS_CHOICES, max_length=9, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.OneToOneField(PatientModel, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='booking')

    # def __str__(self) -> str :
    #     return f'{self.medical_personnel} ==> {self.created_at}'
    
    # def __str__(self)  -> str:
    #     return f'Mr./Mrs. {self.patient.user.first_name} ===> \
    #         {self.patient.phone} ===> {self.patient.genotype} ===> {self.patient.user.email}'

    

    
    def __str__(self) -> str:
        return self.patient.user.email

        # {self.patient.user.phone} {self.patient.user.medical_history}'
    class Meta:
        # ordering = ['created_at']
        permissions = [
            ('cancel_appointment', 'Can cancel appointment')
        ]




















































































        
# class AppointmentPageModel(models.Model):
#     appointment = models.ForeignKey(AppointmentModel, on_delete=models.PROTECT, related_name='appoint')
#     hospital = models.ForeignKey(HospitalModel, on_delete=models.PROTECT, related_name='hospital_detail')
    
# class AppointmentCartModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     created_at = models.DateTimeField(auto_now_add=True)

# class AppointmentCartItemModel(models.Model):
#     STATUS_CHOICES = [ 
#         ('15 minutes', '15 minutes'),
#         ('20 minutes', '20 minutes'),
#         ('30 minutes', '30 minutes'),
    
#     ]
#     hospital = models.ForeignKey(MedicalPersonnel, on_delete=models.CASCADE)
#     booked_time = models.CharField(max_length=20, choices=STATUS_CHOICES, default='15 minutes')
    # class Meta:
    #     unique_together = [['booking_cart', 'hospital']]

