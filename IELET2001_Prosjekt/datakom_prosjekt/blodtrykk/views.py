from .models import Patient
from rest_framework import viewsets

from .serializers import PatientListSerializer, PatientDataSerializer
from .serializers import NurseListSerializer, NurseDataSerializer, NurseUserSerializer
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from .permissions_blodtrykk import IsSuperUser
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required


from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm, AccessToRegistrationForm, PatientForm
from .serializers import PatientListSerializer, PatientDataSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
def UserView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientListSerializer
    queryset = Patient.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer

        if self.action == 'retrieve':
            return PatientDataSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


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


def patients_data_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    context = {'patient': patient}
    return render(request, 'patient_data.html', context)


# The NurseViewSet is used to display the nurses in the database, not the users
"""class NurseViewSet(viewsets.ModelViewSet):
    serializer_class = NurseListSerializer
    queryset = Pasient.objects.all()
    permission_classes = [IsSuperUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return NurseListSerializer

        if self.action == 'retrieve':
            return NurseDataSerializer

        return super().get_serializer_class()"""


class NurseUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NurseUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]


def dashboard(request):
    return render(request, "dashboard.html")


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
        # omdiriger superbrukere til API-roten
        return redirect('/')
    else:
        # omdiriger vanlige brukere til dashboardet
        # Erstatt 'dashboard' med din faktiske dashboard URL navn
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
