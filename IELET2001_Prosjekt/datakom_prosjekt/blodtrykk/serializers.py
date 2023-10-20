from rest_framework import serializers
from . import models


class PasientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pasient
        fields = "__all__"


class PasientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pasient
        fields = ["id", "first_name",]


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
        model = models.Nurse
        fields = ["id", "first_name", "last_name",
                  "birthDate", "phone", "email", "user"]
