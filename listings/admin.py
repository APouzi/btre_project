from django.contrib import admin
from .models import Listing

#Create Superuser & Register Models With Admin -  3:45 so this is basically where we can customize admin stuff for the for the listings app and I want to register register the listing for the admin area. 4:00 So firstly, we want to import Listing from .models. and I'm using listing because in my listings/models.py that's what I called it. So whatever you have here is what you want to have in listings/models.py

#Create Superuser & Register Models With Admin -  4:27 and to register the model, we want to do a admin.site.register(Listing), 4:37 then if we go back to admin area on the site. We should see the listings model. so if I click on listings, we don't have any at the moment, but they would be listed here and we can add them. Notice that we have all of the fields that we added, even realtor, so we can choose a realtor title. From 4:37 to 6:37 he talks about the different fields we inputted in there and how Django gives us alot of features. 

#Create Superuser & Register Models With Admin -  6:22 So I think what I want to do now before we start adding data is also add the realtors in the in the admin area.So to do that, we're going to do the same thing. (6:39 copy the import and one line of code we wrote to paste into realtors/admin)

#Customize Admin Display Data - 00:30 you want to create a class called ListingAdmin and pass in there something called "admin.ModelAdmin". Also we need to pass in "ListingAdmin" into "admin.site.register(Listing)", so it becomes "admin.site.register(Listing, ListingAdmin)"
class ListingAdmin(admin.ModelAdmin):
#Customize Admin Display Data -1:00 so we want to define what we want in the table or in he list. For this we do "list_display", inside we want the fields we want shown. Whats's cool is when you do a bool value, it actually shows you checkbox. After this we see that it was a success
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
#Customize Admin Display Data - 2:31 we can't click on the title to get to the articles there, but I can with ID simply because it's the first one. To change that we are going to have the have the links accepted.   
  list_display_links = ('id', 'title')
#Customize Admin Display Data - 3:40 We want to add a filter box, make sure to put comma at the end if it's only one value. After this, we get a box at the side of the admin page that allows us to filter by realtor.
  list_filter = ('realtor',)
#Customize Admin Display Data - 4:20 Now we want to add in the ability to unpubish ariticles via  the listings page without having to go to every single one of these. We want to set the list_editable to "is_published" 
  list_editable = ('is_published',)
#Customize Admin Display Data - Here we can search fields in regards to these fields below   
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
#Customize Admin Display Data - Now we want to define the listings per page because it was just going to keep going without pagination.  
  list_per_page = 25
admin.site.register(Listing) 
#Customize Admin Display Data - 7:09 Now that we have done the listings go to realtors/admin.py (7:09 go to realtors/admin.py) 