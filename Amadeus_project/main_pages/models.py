from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    username = models.CharField('login', max_length=50, unique=True)
    email = models.CharField('email', max_length=50, unique=True)
