from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F

CHOICES_STATUS = (
        ('simple','Simple'),
        ('team', 'Team'),
        ('core', 'Core'),
        ('admin', 'Admin')
    )

class User(AbstractUser):

    thumbnail = models.ImageField(verbose_name=F('username')+'_pic', blank=True, null=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, db_default='Simple')
    position = models.CharField(max_length=50, blank=True, null=True)



