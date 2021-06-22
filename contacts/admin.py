from django.contrib import admin
#Contacts Admin Customization - 00:16 we want to import the contact models to use this.
from .models import Contact

#Contacts Admin Customization - 00:35 First lets create the class of ContactsAdmin. We want to display the list, which is going to be "id","name","listing","email","contact_date". These are the fields that will be displayed for each input. The links, or how we are going to be able to click on the article to go deeper, is going to be "list_display_links". We then want to input what the search fields are going to be searching. Then we want to know how many per page is going to be inputted and thats going to be 25. END OF VIDEO
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

#Contacts Admin Customization - 00:49 we want to run this through here
admin.site.register(Contact,ContactAdmin)
