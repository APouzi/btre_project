#Listings URLs & Template - 2:24 this is going to be similar to what we did with pages/urls.py, so I'm actually going to just copy that and bring that over to the new one here.

from django.urls import path
from . import views
urlpatterns = [
    # 2:50 if we leave this empty, this will pertain to the /listings method. For the singular listing, we actually want something like "/listings/23" because we want an id number. Because of this we need to include a paramter.
    path('', views.index, name = 'listings'),
    path('about', views.about, name = 'about')
]