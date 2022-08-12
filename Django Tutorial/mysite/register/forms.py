from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # ALWAYS TYPE IT CORRECTLY 
        fields = ["username", "email", "password1", "password2"] # HAD AN ISSUE FOR 15 MINUTES BC THERE WAS NO 'S' AT THE END OF FIELDS

