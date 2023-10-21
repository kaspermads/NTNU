from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings


# Create your models here.


class SensorData(models.Model):
    temperate = models.FloatField()
    pulse = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperate} {self.pulse} {self.timestamp}"


class Pasient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="pasient")


class Nurse(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
