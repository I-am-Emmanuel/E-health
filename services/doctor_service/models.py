from django.db import models


# Create your models here.
class Doctor(models.Model):
    SPECIALTY_CHOICES = (
        ('epidemiologist', 'Epidemiologist'),
        ('general practitioner', 'General practitioner'),
        ('pediatrician', 'Pediatrician'),
        ('dentist', 'Dentist'),
        ('surgeon', 'Surgeon'),
        ('dermatologist', 'Dermatologist'),
        ('plastic surgeon', ' Plastic Surgeon'),
        ('psychiatrist', 'Psychiatrist'),
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES, default='psychiatrist')
    available_days = models.DateTimeField()

    class Meta:
        ordering = ('available_days',)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} {self.specialty} {self.available_days}'
