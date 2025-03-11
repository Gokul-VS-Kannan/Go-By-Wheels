from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('driver', 'Driver'),
        ('mechanic', 'Mechanic'),
        ('partner', 'Partner'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_approved = models.BooleanField(default=False)  # For drivers, mechanics, etc.
    
    def __str__(self):
        return self.username
