"""
URL configuration for datakom_prosjekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from blodtrykk.views import dashboard, register, access_view, redirect_if_user_is_super
from django.contrib import admin
from django.urls import include, path
from . import settings

from blodtrykk.views import PasientViewSet, NurseUserViewSet, pasients_list_view
"""from blodtrykk.views import NurseViewSet"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()
router.register(r'Pasients', PasientViewSet, basename='pasients')
router.register(r'Nurses', NurseUserViewSet, basename='nurse_user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path("access_view/", access_view, name="access_view"),
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("redirect_if_user_is_super/", redirect_if_user_is_super,
         name="redirect_if_user_is_super"),
    path("patients/", pasients_list_view, name="patients"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),


]
urlpatterns += router.urls
