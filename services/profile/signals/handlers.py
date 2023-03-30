# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from profile.models import PatientModel, MedicalPersonnel 

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_patient_profile_for_new_user(sender, **kwargs):
#     if kwargs['created']:
#         PatientModel.objects.create(user=kwargs['instance'])
#         MedicalPersonnel.objects.create(user=kwargs['instance'])
