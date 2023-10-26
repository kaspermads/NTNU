from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


# Create your models here.


class SensorData(models.Model):
    temperate = models.FloatField()
    pulse = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperate} {self.pulse} {self.timestamp}"


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="pasient")
    address = models.CharField(max_length=100, null=True)

    # Image field:
    # pasient_photo = models.ImageField(upload_to='media/patient_photos', null=True, blank=True)

    def save(self, *args, **kwargs):

        super(Patient, self).save(*args, **kwargs)

        # img = Image.open(self.pasient_photo.path)

        # if img.height > 300 or img.width > 300:
        # output_size = (300, 300)
        # img.thumbnail(output_size)
        # img.save(self.pasient_photo.path)

# The model for Nurse


class DailyBloodPressureData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Nurse(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
