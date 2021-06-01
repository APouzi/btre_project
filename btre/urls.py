
from django.contrib import admin
from django.urls import path, include
# 8:24 we want to add the other path from the pages app views.py file. We want to put in whatever we want the first segment of the url to be of the pages app, in this case we don't want it to be anything. So, we don't want it to be "pages/about" we just want it to be "/about" for our url. Make sure to use an include for this and put the "include" next to the path import since we are importing from there. 
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
