from django.shortcuts import render, redirect
from django.contrib import messages, auth
#User Registration - 3:55 bring in the User model from django.contrib.auth.models. Now we can use this model like any other model. If User.objects.filter
from django.contrib.auth.models import User

#Accounts App & URLs - 7:00 now we ware going to be creating register method, we want to pass in the request. inside the method we want to have a return, that is passed in with the request, the template name, 
def register(request):
#Register & Login Templates - 5:10 When the forms get submitted, we need to identify if it's a post or a get. For now, we will just put a placeholder of a print statement and then we want a return of a redirect to register.html. Then if we test something out, like input something into the fields. 7:24 We get rid of the two lines and input a comment in the logic instead. 8:00 He talks aobut how we are going to have the validation from the client side, on the server side, we need to make sure the passwords match. We also need to make sure that there is not an email or username already taken in the system. END OF VIDEO
    if request.method == 'POST':
        # logic
        # print("POST")
        # return redirect('register')


        # messages.error(request, 'Testing error message')
#Message Alerts - 7:59 we are going to be testing if messages are going to be working. To do this we are going to be doing a redirect to register, same page. To output a message, right above it, we are going to input what our message is going to be "messages.error(request, 'Testing error message')" First parameter is the httprequest and the 2nd is going to be the message. 9:00 This message is not going to show up because our partial isn't inserted into the register template. (9:32 go to accounts/register.html)
        # return redirect('register')


#User Registration - 00:11 We are going to be commenting out the test messages we were using and going to be inputting the values we need from the field for the registration. We put "first_name" = and then we input POST instead of GET, so: "request.POST['first_name']" and we input "first_name" because we want that inputed into the post. Then we want to take care of the other fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
#User Registration - 1:44 we now want to check if passwords match. Then we want to do an else statement right away, which essentially brings up an error message saying that the passwords do not match, that will be followed up by a return of a redirect that redirects us to "register". 2:57 now lets try and see if this works. It works and disappears right after.
        if password == password2:
#User Registration - 3:23 now if they do match, we have more validation to do. firstly being, we need to check the username. to do this,we need to bring in the user model, we didnt' create the user model but it comes with django. So to use it we need to bring it in (go to the top)
      # Check username
#User Registration - 4:17 We are going to start this off with an if statement asking if username from the user object is the same username from the post here. Then ask if it exists. If it's true, it exists, then we want to get an error message saying that the username already exists. Have a return of a redirect to the same page.
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
#User Registration - 5:20 If there is no username, then we want to continue on to the next set of validation, the email. So samething like above, if this passes then we want to create that user because all has passed.
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
#User Registration - 6:21 We want to test these, as far as users go. We have one user, which is alex and with an email of alex@squat.xyz. We should not be able to register with either of those. After testing this out we move on to creating the users.
                else:
#User Registration - 8:00 To do the creation, we are going to create a variable called user, pass in all the fields that we want. 8:50 if we want to log in the user once they are registered, we can just simply say "auth.login(request, user)" right after, also a message.success to let the user know they logged in. If we want to use the Auth object, we need to bring it in and it's part of Django.contrib. 9:19 attach "auth" to the end of "from django.contrib import messages" on line 2. We comment this out as it's one way to do it. 
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
            # Login after register
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
#User Registration - 10:30 If we don't want to log them in, then we can just do "user.save", with a message of success, along with the success message and a redirect to the login page. 11:06 Try this out to see if it works, it does work and you see a new user available right away. Password is also hashed automatically, as Django takes care of that. 12:20 We want to make sure that the index has the alerts available. (12:30 go to templates/pages/index.html)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')    

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
