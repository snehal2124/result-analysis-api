from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    type = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
