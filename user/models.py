from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from .manger import CustomUserManger

class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    user_type = models.SmallIntegerField(default=1, choices=[
        (1, 'user'),
        (2, 'admin'),
        (3,'derektor')
    ])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_name = False
    first_name = False

    REQUIRED_FIELDS = ['phone', 'email']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    objects = CustomUserManger()

    class Meta:
        verbose_name = 'Foydalanuvci'
        verbose_name_plural = 'Foydslsnuvchilar'