from django.db import models


# Create your models here.

# class Gender(model.models)

class PatientModel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Other'),
    ]

    BLOOD_GROUP_A_POSITIVE = 'A+'
    BLOOD_GROUP_A_NEGATIVE = 'A-'
    BLOOD_GROUP_B_POSITIVE = 'B+'
    BLOOD_GROUP_B_NEGATIVE = 'B-'
    BLOOD_GROUP_O_POSITIVE = 'O+'
    BLOOD_GROUP_O_NEGATIVE = 'O-'
    BLOOD_GROUP_AB_POSITIVE = 'AB+'
    BLOOD_GROUP_AB_NEGATIVE = 'AB-'

    BLOOD_GROUP_CHOICES = [
        (BLOOD_GROUP_A_POSITIVE, 'A+'),
        (BLOOD_GROUP_A_NEGATIVE, 'A-'),
        (BLOOD_GROUP_B_POSITIVE, 'B+'),
        (BLOOD_GROUP_B_NEGATIVE, 'B-'),
        (BLOOD_GROUP_O_POSITIVE, 'O+'),
        (BLOOD_GROUP_O_NEGATIVE, 'O-'),
        (BLOOD_GROUP_AB_NEGATIVE, 'AB+'),
        (BLOOD_GROUP_AB_NEGATIVE, 'AB-'),
    ]

    GENOTYPE_AA = 'AA'
    GENOTYPE_AS = 'AS'
    GENOTYPE_AC = 'AC'
    GENOTYPE_SS = 'SS'
    GENOTYPE_SC = 'SC'

    GENOTYPE_CHOICES = [
        (GENOTYPE_AA, 'AA'),
        (GENOTYPE_AS, 'AS'),
        (GENOTYPE_AC, 'AC'),
        (GENOTYPE_SS, 'SS'),
        (GENOTYPE_SC, 'SC'),
    ]

    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    address = models.CharField(max_length=250, null=False)
    blood_group = models.CharField(max_length=6, choices=BLOOD_GROUP_CHOICES, blank=False)
    genotype = models.CharField(max_length=11, choices=GENOTYPE_CHOICES, blank=True)
    patient_phone = models.CharField(max_length=14)
    # medical_history = models.CharField()
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
