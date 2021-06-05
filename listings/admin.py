from django.contrib import admin
from .models import Listing

#Create Superuser & Register Models With Admin -  3:45 so this is basically where we can customize admin stuff for the for the listings app and I want to register register the listing for the admin area. 4:00 So firstly, we want to import Listing from .models. and I'm using listing because in my listings/models.py that's what I called it. So whatever you have here is what you want to have in listings/models.py

#Create Superuser & Register Models With Admin -  4:27 and to register the model, we want to do a admin.site.register(Listing), 4:37 then if we go back to admin area on the site. We should see the listings model. so if I click on listings, we don't have any at the moment, but they would be listed here and we can add them. Notice that we have all of the fields that we added, even realtor, so we can choose a realtor title. From 4:37 to 6:37 he talks about the different fields we inputted in there and how Django gives us alot of features. 

#Create Superuser & Register Models With Admin -  6:22 So I think what I want to do now before we start adding data is also add the realtors in the in the admin area.So to do that, we're going to do the same thing. (6:39 copy the import and one line of code we wrote to paste into realtors/admin)

admin.site.register(Listing) 