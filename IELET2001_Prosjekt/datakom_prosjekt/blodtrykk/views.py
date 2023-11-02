# Importing the basics
from .models import Patient, DailyBloodPressureData
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect

# Importing serializers
from .serializers import PatientListSerializer, PatientDataSerializer, PatientBloodPressureDataSerializer, NurseUserSerializer

# Importing decorators
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Importing authentication and permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


# Importing forms, such as the built in UserCreationForm
from .forms import CustomUserCreationForm, AccessToRegistrationForm, PatientForm


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientListSerializer
    queryset = Patient.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer

        if self.action == 'retrieve':
            return PatientDataSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


# The patients_list_view is used to display the patients in the database while requiring authentication and login
@permission_classes([IsAuthenticated])
@login_required
def patients_list_view(request):
    patients = Patient.objects.all()
    patients_data = [
        {

            "id": patients.id,
            "first_name": patients.first_name,
            "last_name": patients.last_name,
            "birthDate": patients.birthDate,
            "phone": patients.phone,
            "added_by": patients.added_by,

        } for patients in patients
    ]

    context = {'patients': patients_data}
    return render(request, 'view_patients.html', context)


# The patients_data_view is used to display the patients data in the database while requiring authentication and login
@permission_classes([IsAuthenticated])
@login_required
def patients_data_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient_blood_pressure_data = DailyBloodPressureData.objects.all().filter(patient=patient)
    context = {'patient': patient,
               'patient_blood_pressure_data': patient_blood_pressure_data}
    return render(request, 'patient_data.html', context)


# The PostDailyBloodPressureData is used to view the daily blood pressure data sent from the ESP32
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def PostDailyBloodPressureData(request):
    if request.method == 'POST':
        serializer = PatientBloodPressureDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class NurseUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NurseUserSerializer
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissions]


def dashboard(request):
    return render(request, "dashboard.html")


# The access_view is used to grant access to the registration page
ACCESS_CODE = "2441"


def access_view(request):
    if request.method == 'POST':
        form = AccessToRegistrationForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data["access_code"]
            if access_code == ACCESS_CODE:
                request.session["access_granted_to_register"] = True
                return redirect(reverse("register"))
            else:
                form.add_error("access_code", "Wrong access code")
    else:
        form = AccessToRegistrationForm()
    return render(request, "access_form.html", {"form": form})

# The register view is used to register a new nurse


# The register view is used to register a new nurse
def register(request):
    if not request.session.get("access_granted_to_register"):

        return redirect(reverse("access_view"))

    if request.method == "GET":
        return render(
            request, "register_nurse.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            # fjerner nøkkelen etter vellykket registrering
            del request.session['access_granted_to_register']

            return redirect(reverse("dashboard"))


def redirect_if_user_is_super(request):
    if request.user.is_superuser:
        return redirect('/')
    else:

        return redirect(reverse('dashboard'))

# The register_pasient view is used to register a new pasient


@login_required
def register_patient(request):
    if request.method == "GET":
        return render(
            request, "register_patient.html",
            {"form": PatientForm}
        )
    elif request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.added_by = request.user
            patient.save()

            return redirect(reverse("patients"))
    else:
        form = PatientForm()
    return render(request, "register_patient.html", {"form": form})
