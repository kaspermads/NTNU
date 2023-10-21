from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PasientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pasient
        fields = "__all__"


class PasientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pasient
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
