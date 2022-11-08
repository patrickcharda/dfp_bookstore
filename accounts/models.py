from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # mobile = models.CharField(max_length=10)
    # REQUIRED_FIELDS = ["mobile", "email"]
