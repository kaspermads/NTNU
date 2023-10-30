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
    patient_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.DailyBloodPressureData
        fields = ["patient_id", "systolic", "diastolic", "pulse", "timestamp"]

    def validate_patient_id(self, patient_id):
        try:
            models.Patient.objects.get(id=patient_id)
            return patient_id
        except models.Patient.DoesNotExist:
            raise serializers.ValidationError("Patient does not exist")

    def create(self, validated_data):
        patient_id = validated_data.pop("patient_id")
        patient = models.Patient.objects.get(id=patient_id)
        blood_pressure_data = models.DailyBloodPressureData.objects.create(
            patient=patient, **validated_data)
        return blood_pressure_data


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
