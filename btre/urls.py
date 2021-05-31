"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# 8:24 we want to add the other path from the pages app views.py file. We want to put in whatever we want the first segment of the url to be of the pages app, in this case we don't want it to be anything. So, we don't want it to be "pages/about" we just want it to be "/about" for our url. Make sure to use an include for this and put the "include" next to the path import since we are importing from there. 
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
