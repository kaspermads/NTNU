from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

import random
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    """added_by = models.ForeignKey(
        # Dette peker på modellen som håndterer brukere i ditt Django-prosjekt.
        settings.AUTH_USER_MODEL,
        # Dette vil tillate tilgang til pasienter via User-instanser (f.eks., user.pasienter.all()).
        related_name='pasienter',
        # Hvis brukeren slettes, vil deres pasienter også slettes.
        on_delete=models.CASCADE"""


class Nurse(models.Model):

    """user = models.OneToOneField(User, on_delete=models.CASCADE)"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    """password = models.CharField(max_length=100, help_text="Enter password")"""

    """def save(self, *args, **kwargs):
        if self.pk is None:  # Dette betyr at en ny oppføring blir opprettet
            # Her oppretter du en ny bruker
            user = User.objects.create_user(
                username=self.email,  # Vanligvis bruker vi e-post som brukernavn
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
                email=self.email
            )
            self.user = user
        super(Nurse, self).save(*args, **kwargs)"""
