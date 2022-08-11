from django.contrib import admin
from .models import ToDoList, Items
# Register your models here.

admin.site.register(ToDoList) # This is to import the data into the admin dashboard 
admin.site.register(Items)