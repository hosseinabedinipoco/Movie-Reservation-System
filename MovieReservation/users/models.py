from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username