from django.contrib import admin
from .models import Realtor
#Create Superuser & Register Models With Admin - 6:54 paste code here. Then the admin area shows that we have Realtor functionality after we refresh the page. So now that means we have realtors and listings as part of the admin area. Later we will customize the admin area, we can specifiy how data including the listings is shown. We have alot of control in this regard

#Customize Admin Display Data - 7:09 here we are going to be changing what is viewed with list_display, then have the id and name be the links to access the invidual realtors. Then on top of that we will have only 25 displayed at a time.
class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'hire_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25
admin.site.register(Realtor) 
