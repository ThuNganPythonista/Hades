from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from src.public.apps.user.CustomUserManager import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    # form em ko có username nên em đặt nó None
    # Còn lại thì đều có các trường của nó
    email = models.EmailField(_("email address"), blank=True, unique=True)
    gender = models.BooleanField(default=False, blank=False)
    birth_day = models.DateField(auto_created=True, default=timezone.now())
    fullname = models.CharField(max_length=100, default='', blank=False)
    avatar = models.ImageField(upload_to='avatar', blank=True)

    USERNAME_FIELD = "email"
    # cái tên account
    REQUIRED_FIELDS = ['gender', 'fullname']

    objects = CustomUserManager()

    def __str__(self):
        return self.email