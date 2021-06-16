from django.shortcuts import render, redirect

#Accounts App & URLs - 7:00 now we ware going to be creating register method, we want to pass in the request. inside the method we want to have a return, that is passed in with the request, the template name, 
def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/register.html')

#Accounts App & URLs -8:00 logout isn't going to be a render but a redirect to index. Make sure to bring that into the imports from shortcuts.
def logout(request):
    return render('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
#Accounts App & URLs - 8:52 after finishing all the methods, we want to (accounts/go to urls.py)
