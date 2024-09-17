from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    user_id = models.IntegerField(unique=True, default='111')
    password = models.CharField(max_length=255, blank=True)
