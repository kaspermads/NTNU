from .models import Pasient
from rest_framework import viewsets

from .serializers import PasientListSerializer, PasientDataSerializer
from .serializers import NurseListSerializer, NurseDataSerializer, NurseUserSerializer
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from .permissions_blodtrykk import IsSuperUser
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm, AccessToRegistrationForm, PasientForm
from .serializers import PasientListSerializer, PasientDataSerializer


# Create your views here.
def UserView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)


class PasientViewSet(viewsets.ModelViewSet):
    serializer_class = PasientListSerializer
    queryset = Pasient.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return PasientListSerializer

        if self.action == 'retrieve':
            return PasientDataSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


def pasients_list_view(request):
    pasients = Pasient.objects.all()
    pasients_data = [
        {

            "id": pasients.id,
            "first_name": pasients.first_name,
            "last_name": pasients.last_name,
            "birthDate": pasients.birthDate,
            "phone": pasients.phone,
            "added_by": pasients.added_by,

        } for pasients in pasients
    ]

    context = {'pasients': pasients_data}
    return render(request, 'view_pasients.html', context)


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
def register_pasient(request):
    if request.method == "GET":
        return render(
            request, "register_pasient.html",
            {"form": PasientForm}
        )
    elif request.method == "POST":
        form = PasientForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            return redirect(reverse("patients"))
    else:
        form = PasientForm()
    return render(request, "register_pasient.html", {"form": form})
            

           
