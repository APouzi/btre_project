#Creating the Pages App - 4:10 now we are going to be importing paths from the django module. This is because we have to do this anytime we want to introduce paths. 
from django.urls import path
# Then we want to bring in the views, the idea is that we want a route/path/route, whatever you want to call it, that is attatched to a method inside the view file, so we want a URL for our homepage.
from . import views
#Creating the Pages App - 5:30 The path we want is a the homepage and that means nothing. First the first parameter, leave it empty, Some frameworks will have you use "/" but here it's just nothing. 2nd paramter has us name the method we want to connect in the view and the third parameter is the name of the path, to easily access. (6:21 - go to views.py)
urlpatterns = [
    path('', views.index, name = 'index')
]