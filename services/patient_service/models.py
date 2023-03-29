from django.db import models


# Create your models here.
class Patient(models.Model):
    SPECIALTY_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=10, choices=SPECIALTY_CHOICES, default='other')

    class Meta:
        ordering = ('gender',)

    def __str__(self):
        return f'{self.last_name} - {self.last_name} - {self.date_of_birth} - {self.gender}'
