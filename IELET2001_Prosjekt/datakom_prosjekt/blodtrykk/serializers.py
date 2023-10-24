from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"


class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ["id", "first_name", "added_by"]


class NurseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nurse
        fields = "__all__"


class NurseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nurse
        fields = "__all__"


class NurseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "email"]
