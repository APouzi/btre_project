from django.contrib import admin
from .models import Realtor
#Create Superuser & Register Models With Admin - 6:54 paste code here. Then the admin area shows that we have Realtor functionality after we refresh the page. So now that means we have realtors and listings as part of the admin area. Later we will customize the admin area, we can specifiy how data including the listings is shown. We have alot of control in this regard

admin.site.register(Realtor) 
