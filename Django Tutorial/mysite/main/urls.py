from django.urls import path
from . import views # Pretty much import views from the current directory

urlpatterns = [
path("", views.index, name = "index"), # If we get in the application and we're in the homepage, go to the views index page 
                                        # (http://127.0.0.1:8000)
path("v1/", views.v1, name = "view 1") # ("The path that we're looking for in view.py", the function in the views module, name = IDK what this part does) 
                                        # (http://127.0.0.1:8000/v1/)
]