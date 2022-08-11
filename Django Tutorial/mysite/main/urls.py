from django.urls import path
from . import views # Pretty much import views from the current directory

urlpatterns = [
path("", views.index, name = "index"), # If we get in the application and we're in the homepage, go to the views index page
path("v1/", views.v1, name = "random random") # ("The path that we're looking for in view.py", the function in the views module, )
]