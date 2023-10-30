from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PatientListSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField()

    class Meta:
        model = models.Patient
        fields = "__all__"

    def get_added_by(self, obj):
        return obj.added_by.get_full_name() if obj.added_by else "None"


class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ["id", "first_name", "added_by"]

    def get_added_by(self, obj):
        return obj.added_by.get_full_name() if obj.added_by else "None"


class PatientBloodPressureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailyBloodPressureData
        fields = ["patientID", "systolic", "diastolic", "pulse", "timestamp"]


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
