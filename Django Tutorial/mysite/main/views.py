from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import ToDoList, Items
from .forms import CreateNewList
# Create your views here.

# Create a function that represent the view

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.items_set.all():
                if response.POST.get(c + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.items_set.create(text = txt, complete = False)
            else:
                print("invalid")
    return render (response, "main/list.html", {"ls":ls})

def home(response):
    return render (response, "main/home.html", {}) # After setting the path, it renders "main/home.html" which uses the base.html as extension (check home.html file)

def create(response):
    if response == "POST":
        form = CreateNewList(response.POST) # All the info from the form 
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n )
            t.save()
        return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render (response, "main/create.html", {"form": form})

