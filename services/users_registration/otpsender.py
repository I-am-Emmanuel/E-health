from django.core.mail import send_mail, mail_admins, BadHeaderError
from rest_framework.response import Response
import random
from django.conf import settings
from . models import User

def sendOtp(email):
    try:
        subject = 'Your account verification email'
        otp = random.randint(100000, 999999)
        message = f'Your otp is {otp}'
        email_from = settings.EMAIL_HOST
        # send_mail(subject, message, 'olaifaemmanuel@gmail.com', [email])
        # mail_admins(subject, html_message=message)
        send_mail(subject, message, email_from, [email])
        user_object = User.objects.get(email=email)
        user_object.otp = otp
        user_object.save()
    except BadHeaderError:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return user_object
