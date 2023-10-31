from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PatientListSerializer(serializers.ModelSerializer):
    added_by = serializers.SerializerMethodField()

    class Meta:
        model = models.Patient
        fields = "__all__"

    # Overrides the get_added_by method to return the full name of the user who added the patient
    def get_added_by(self, obj):
        return obj.added_by.get_full_name() if obj.added_by else "None"


class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ["id", "first_name", "added_by"]

    # Overrides the get_added_by method to return the full name of the user who added the patient
    def get_added_by(self, obj):
        return obj.added_by.get_full_name() if obj.added_by else "None"


class PatientBloodPressureDataSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.DailyBloodPressureData
        fields = ["patient_id", "systolic", "diastolic", "pulse", "timestamp"]

    # Validates that the patient_id is valid and checks if the patient exists
    def validate_patient_id(self, patient_id):
        try:
            models.Patient.objects.get(id=patient_id)
            return patient_id
        except models.Patient.DoesNotExist:
            raise serializers.ValidationError("Patient does not exist")

    # Overrides the create method to create a new DailyBloodPressureData object with the patient_id sent in the request.
    # The patient_id is removed from the validated_data and the patient is fetched from the database.
    # The DailyBloodPressureData object is then created with the patient and the validated_data.
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
