from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .manager import UserModelManager


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserModelManager()

    def __str__(self):
        return self.email


