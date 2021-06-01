from django.shortcuts import render
from django.http import HttpResponse
#Creating the Pages & Base Layout - 6:25 Lets create the function for the urls.py, after that import HttpResponse from the django http package. For now we ware just going to be using HttpResponse for example. @7:40 This isn't going to work because we still need to take the urls.py file and go to the other urls.py file and make some changes there (8:10 Go to urls.py in BTRE)

#@2:41 we want to make sure that we have the render instead of the HttpResponse that we had. Create that about function for the about path.
def index(request):
    return render(request, 'pages/about.html')

def about(request):
    return render(request, 'pages/about.html')