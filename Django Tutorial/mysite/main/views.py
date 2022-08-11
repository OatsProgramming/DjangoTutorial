from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items
# Create your views here.

# Create a function that represent the view

def index(response, id):
    ls = ToDoList.objects.get(id = id)

    return render (response, "main/list.html", {"ls":ls})

def home(response):
    return render (response, "main/home.html", {}) # After setting the path, it renders "main/home.html" which uses the base.html as extension (check home.html file)