from django.shortcuts import render, redirect

#Accounts App & URLs - 7:00 now we ware going to be creating register method, we want to pass in the request. inside the method we want to have a return, that is passed in with the request, the template name, 
def register(request):
#Register & Login Templates - 5:10 When the forms get submitted, we need to identify if it's a post or a get. For now, we will just put a placeholder of a print statement and then we want a return of a redirect to register.html. Then if we test something out, like input something into the fields. 7:24 We get rid of the two lines and input a comment in the logic instead. 8:00 He talks aobut how we are going to have the validation from the client side, on the server side, we need to make sure the passwords match. We also need to make sure that there is not an email or username already taken in the system. END OF VIDEO
    if request.method == 'POST':
        # logic
        # print("POST")
        # return redirect('register')
        return
    else:
        return render(request, 'accounts/register.html')
 
def login(request):
    if request.method == 'POST':
        # logic
        # print("POST")
        # return redirect('register')
        return
    else:
        return render(request, 'accounts/login.html')

#Accounts App & URLs -8:00 logout isn't going to be a render but a redirect to index. Make sure to bring that into the imports from shortcuts.
def logout(request):
    return render('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
#Accounts App & URLs - 8:52 after finishing all the methods, we want to (accounts/go to urls.py)
