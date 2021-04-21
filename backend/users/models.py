from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('admin', 'admin'),
        ('teacher', 'teacher'),
        ('student', 'student')
    )
    role = models.CharField(choices=ROLES, max_length=20, default='student')
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
