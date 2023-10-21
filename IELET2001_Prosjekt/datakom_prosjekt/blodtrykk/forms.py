from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + \
            ("email", "first_name", "last_name")


class AccessToRegistrationForm(forms.Form):
    access_code = forms.CharField(
        max_length=32, required=True, label="Access code")
