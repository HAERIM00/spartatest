
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomModel(AbstractBaseUser):
    address = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    db_table = 'custom_user'