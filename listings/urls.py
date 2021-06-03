#Listings URLs & Template - 2:24 this is going to be similar to what we did with pages/urls.py, so I'm actually going to just copy that and bring that over to the new one here.

from django.urls import path
from . import views
urlpatterns = [
#Listings URLs & Template -  2:50 if we leave this empty, this will pertain to the /listings method. For the singular listing, we actually want something like "/listings/23" because we want an id number. Because of this we need to include a paramter, in that parameter, we want to put in "<int: listing_id>". Then we willc change the 2nd parameter to "views.listing" and then the name is going to be "listing".
    path('', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
#Listings URLs & Template - 3:49 the last url, is going to be one for the search, And the reason we're not putting in listings/search here is because we're actually going to link this to the main btre/urls.py, and tell it that anything that has listings/ should look at this file, we will have some errors because we haven't created these methods yet (4:24 go to btre/urls.py)
    path('search', views.search, name="search") 
]