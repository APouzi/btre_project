
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#Creating The Pages App - 8:24 we want to add the other path from the pages app views.py file. We want to put in whatever we want the first segment of the url to be of the pages app, in this case we don't want it to be anything. So, we don't want it to be "pages/about" we just want it to be "/about" for our url. Make sure to use an include for this and put the "include" next to the path import since we are importing from there. Now, we should be able to access the index because we left the path index empty '' in "path('', include('pages.urls'))".
urlpatterns = [
    path('', include('pages.urls')),
#Listings URLs & Template - 4:34 We want to do the same thing we did with pages.urls. (5:03 now we need to go to our settings.py to get our app inputted)
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Media Folder & Adding Data 1:35 We are going to do something alittle odd here, with a " + Static....", we are going to be populating them with the information below, we will be getting an error unless we bring in static and settings with imports. "from django.conf import settings" and from "django.conf.urls.static import static". These steps are the stseps we needed to do for media to show up on the front end. We needed to set up the settings.py Root variables we defined and inputted above and then come in here and add on to the urlpatterns. (3:17 go back to Admin area on localhost to start adding realotrs, listings and media)
#Media Folder & Adding Data 4:40 Now the reason why after we add a realtor and we even see his name when looking at the list in the admin area, is because of how the object views itself in realtor/models.py. " def __str__(self):...." is set to name. This applies to other places as well, and it wouldn't be like that if we didn't add in that function. Then we add the other two. We added all the listings of the houses with the photos and realtors assigned. END OF VIDEO
