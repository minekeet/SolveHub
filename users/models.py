from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('network', 'Network Team'),
        ('elearning', 'E-learning Team'),
        ('development', 'Development Team'),
    ]
    is_customer=models.BooleanField(default=False)
    is_engineer=models.BooleanField(default=False)
    is_technician=models.BooleanField(default=False)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username



