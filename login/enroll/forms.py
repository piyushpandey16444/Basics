from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(
        max_length=50, label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        labels = {
            "email": "Email"
        }


# class LoginForm
