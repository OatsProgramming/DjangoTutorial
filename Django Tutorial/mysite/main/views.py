from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items
# Create your views here.

# Create a function that represent the view

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    items = ls.items_set.get(id = 1)
    return HttpResponse(f'<h1>{ls.name}</h1><br></br><p>{items.text}</p>')

