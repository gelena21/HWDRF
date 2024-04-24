from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар",
                               blank=True,
                               null=True)
    phone_number = models.CharField(max_length=35, verbose_name="номер телефона",
                                    blank=True,
                                    null=True)
    city = models.CharField(max_length=150, verbose_name="город",
                            blank=True,
                            null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
