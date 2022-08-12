from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.

def register(response):
    if response.method == "POST":
            form = RegistrationForm(response.POST) # Save the new user into the database
            if form.is_valid():
                form.save() 
            return redirect("/home") # After creating a new account, the user will return to the homepage
    else:
        form = RegistrationForm()
    return render(response, "register/register.html", {"form": form} )