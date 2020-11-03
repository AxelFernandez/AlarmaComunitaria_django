from django.conf import settings
from django.db import models

# Create your models here.


class Alarm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True, default='')
    alarm_type = models.CharField(max_length=100, null=True, blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)


class UserExtension(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True, default='')
    phone = models.CharField(max_length=100, null=True, blank=True, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
