#Accounts App & URLs - 5:29 copy and paste from listings, or some other one.
from django.urls import path
from . import views
urlpatterns = [
#Accounts App & URLs - 5:46 We are going to be needing four different urls. loging, register, dashboard, logout. 6:49 now we have to go to views.py and create the methods. (6:52 go to accounts/views.py). 
#Accounts App & URLs - 9:30 in the video, he forgot to bring in the urls.py route in the btre/urls.py (9:39 go to btre/urls.py)
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('dashboard', views.dashboard, name="dashboard"), 
]