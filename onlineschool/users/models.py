from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from lessons.models import Sinflar

from .managers import CustomUserManager

GENDER_CHOICES=(
    ("Erkak","Erkak"),
    ("Ayol","Ayol")
)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'))
    phone = models.CharField(_('phone_number'),max_length=14, unique=True)
    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=5)
    name = models.CharField(_('name'), max_length=15)
    lastname = models.CharField(_('lastname'), max_length=15)
    sinf = models.ForeignKey(Sinflar, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users-image/")

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username', 'name', 'sinf']

    objects = CustomUserManager()
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.name + ' ' + self.lastname

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
