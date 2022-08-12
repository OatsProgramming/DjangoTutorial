from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model): # We're creating a database object which is called ToDoList
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # Every ToDoList will be linked to some kind of user
    name = models.CharField(max_length = 200) # When creating a string, you will always need the max_length

    def __str__(self):
        return self.name # whenever we want to see what it looks like

class Items(models.Model):
    # The reason is Django doesnt know what type of field ToDoList would be
    # on_delete is just saying, well, if we delete to do list, since all items exist on a to do list, we're going to have to delete these as well. 
    # It's just to finding the fact that this has a special way of being removed
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300) 
    complete = models.BooleanField() # Checks whether or not we've completed the item on the ToDoList

    def __str__(self):
        return self.text

# After doing this, we need to tell Django that we've modified the models
# python3 manage.py makemigrations
# This is similar to the git stage when editing code

# python3 manage.py migrate
# This is to make the changes permanent

# After you can check the migrations folder
# There you'll see all the previous changes