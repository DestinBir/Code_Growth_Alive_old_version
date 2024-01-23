from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models import F
from django.db.models.query import QuerySet

"""class User(AbstractUser):
    thumbnail = models.ImageField(verbose_name=F('username')+'_pic', blank=True, null=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, db_default='Simple')
    position = models.CharField(max_length=50, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedIn_link = models.URLField(blank=True, null=True)
"""

class User(AbstractUser):
    class Role(models.TextChoices):
        SIMPLE = "Simple", "Simple"
        TEAM = "Team", "Team"
        ADMIN = "Admin", "Admin"

    base_role = Role.SIMPLE

    role = models.CharField(max_length=20, choices=Role.choices)

    thumbnail = models.ImageField(blank=True, null=True, upload_to='users')
    position = models.CharField(max_length=50, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedIn_link = models.URLField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class TeamManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEAM)


class Team(User):
    base_role = User.Role.TEAM

    team = TeamManager()

    class Meta:
        proxy = True


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ADMIN)


class Admin(User):
    base_role = User.Role.ADMIN

    admin = AdminManager()

    class Meta:
        proxy = True
