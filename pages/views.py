from django.shortcuts import render
from django.http import HttpResponse
#Creating the Pages & Base Layout - 6:25 Lets create the function for the urls.py, after that import HttpResponse from the django http package. For now we ware just going to be using HttpResponse for example. @7:40 This isn't going to work because we still need to take the urls.py file and go to the other urls.py file and make some changes there (8:10 Go to urls.py in BTRE)

#Pages Templates & Base Layout - @2:41 we want to make sure that we have the render instead of the HttpResponse that we had, so replace that with the return of the render function/method and pass in the request and route. Create that "about" function for the about path. (3:40 he goes to urls.py and then saves again to refresh, nothing too important. He says to always make sure we are in the virtual env)(4:30 he is done checking out the sites working and goes to urls.py)
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')