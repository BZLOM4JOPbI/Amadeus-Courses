from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    username = models.CharField('Логин',
                                max_length=50,
                                unique=True,)

    email = models.CharField('Почта',
                            max_length=100,
                            unique=True)

    password = models.CharField('Пароль',
                                max_length=100)

    confirm_password = models.CharField('Подтвеждение пароля',
                                        max_length=100,
                                        blank=True)
    
    pos = models.IntegerField('ID',
                        blank=False,
                        null=True)
                
    
    progress = models.CharField('Прогресс', max_length=10, blank=False)
