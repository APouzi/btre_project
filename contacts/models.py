from django.db import models
from datetime import datetime

# Create your models here.
#Contacts App & Model - 00:46 lets create a class called contact and we need to pass in models.Model
class Contact(models.Model):
#Contacts App & Model - 1:12 Here we are going to be doing a listing and we are not going to be doing a relationship between the contact and the listing, as it's not needed, becayse we only need the listing_id.
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
#Contacts App & Model - 2:21 Messages are going to be optional, so they can be blank.  
    message = models.TextField(blank=True)
#Contacts App & Model - 2:29 we want to have the default be the time of posting. He also added "black = True" idk why
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
# 3:19 the user id is going to be connected to whoever is logged in, who is making an inquiry. We are also setting the blank to true because the person may not be logged in. 
    user_id = models.IntegerField(blank=True)
#Contacts App & Model - 4:09 Then we want this to identify as self. 4:21 now we need to create a migration. 
    def __str__(self):
        return self.name

#Contacts App & Model - 4:49 (go to btre/settings.py and put this app in the installed_apps.) 5:20 go to terminal and type in "python manage.py makemigrations contacts" and then we run a "python manage.py migrate", if we wanted to double check this, we can go to pgadmin and deal with that, through there.