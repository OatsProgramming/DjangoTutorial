from django.urls import path
from . import views # Pretty much import views from the current directory

urlpatterns = [
path("<int:id>", views.index, name="index"), # With <int:id>, were going to look for some integer in our path and pass it to the function used in views.index
# Now, when running this on the website, it would give an error unless you do http://127.0.0.1:8000/"ENTER ANY NUMBER HERE"
# Once you do, it would show any number that you input in a different page

path('', views.home, name='home') # Since its an empty string, this will automatically direct to views.py function home (check views.py to continue)
]