# ----------------------------------Section 5: Apps, URLs & Templates-------------------------------------
# Creating the Pages App - 1:22 When we make a projectapp we have an __init__.py file and it's empty. We don't have to worry about it. Migration's is for any database. Migration's we create we're not going to have any migration's for this particular app, but we will in some of the other ones. Admin is if you want to like you want to show stuff in the admin area. We're not going to need to do that here in our listings app, We will, because we'll want to want to manage our listings from the admin area, but we won't touch this one. And then app.py, this shows you the class of the config. This will actually have to go in our settings file. Models, this is where we create our models. This particular app doesn't have a model, but for instance, "listings" will have like the the the title, the address, the number of bedrooms, all that stuff is going to be defined inside of a model. Then we have our tests if we want to run any tests and a views.py file where we can create methods and we can actually link you URLs to those methods.
#Creating the Pages App - 4:10 we want to go and create the URL file and then go to it (4:10 create a urls.py inside the pages app and go to it)


# Pages Templates & Base Layout - 00:00 You want to go to settings.py to make changes to the Directory so we can allow templates to be used. (:32 go to Settings.py)


# Static Files & Paths - 00:00 We want to handle static files. Then we want to go to the btre_resources folder we downloaded and put in our doc folder. "C:\Users\dimit\Documents\btre_resources\btre_theme\dist\assets". This has all our CSS and such. We want to bring these in as static assets. What we do is we go into the btre_project > btre, and inside the btre folder NOT btre_project folder, we create a directory called "static" and in there we move the whole CSS, JS and Fonts folders but for images we don't want them all(yet), we just want the lightbox and the images there without the folders. We then create a directory in the static called "img" and put all the images in there. (2:23 Now we want to go to our btre/setting.py file, bottom of file)


# Bootstrap Layout Markup - 00:23 So now what I want to do is start to implement our bootstrap theme. So I'm on my base HTML layout, which is in the templates folder and we're going to start adding stuff to this this file from our bootstrap theme. Now, the way that brad does this is with sublime text, which is a different text editor. Brad opens up the bootstrap theme in sublime text. That way I don't get confused by which is which. So I'll know that if it's sublime text, it's just the theme, just the HTML. And our main project is in VST code. So you don't have to do this if you want to open it in the same text editor or something else.( 1:43 go to C:\Users\dimit\Documents\btre_resources\btre_theme\dist and open that folder as workspace folder in notepad++)


# Index, About & Linking - 00:00 We start in the index.html file and we start at the head.. (1:48 go to index.html in notepad++, dist/index.html, then go to index.html and paste them in there.) what I'm going to do is copy everything that we don't have that we didn't put into the base.html. Start above the footer and go all the way up until we are under the navbar. Copy all that and this is going to go and in the index html. 1:01 Now, remember, right now, everything is just static. It's like this form is obviously not going to work. We're not going to get the latest listings. We haven't even installed a database yet. We just want to get the markup to show. And it's going to be like that for quite a while until we get into creating our models and all that stuff. So just keep that in mind. (1:43 go to index.html)


# Listings URLs & Template - 00:00 I want to create our listings app and also our realtors app. so once we do this, we should have two new folders, listings and realtors, and it'll be similar to the pages folder structure with all the the admin.y, the apps, models, test, URLs and views. actually URLs we create ourselves. So let's go ahead and generate these apps. Make sure you're in your virtual environment . We're going to say "python manage.py startapp listings" this will create an app called listings. You can see it created a folder called Listings. Let's do the same with realtors, "python manage.py startapp realtors". Realtors is more just for the model. We're not going to have any templates or views for realtors, It's just to basically to be able to add realtors through the admin area and then basically form a relationship between the realtor and the listing. So let's start off by adding our listings templates. 
# Listings URLs & Template - 1:38  So we're going to go into the templates and let's create a special folder for listing templates (1:38 create a folder in templates called listings, put inside listing.html, listings.html, search.html). Create a file called listing.html, singular, that's for the single listing page.1:48 We also want listings, plural, for, the list of listings And let's also create one called search.html. For listings. We're going to have to have some some URLs, that we need to connect to. So that means we need to create its own URLs.py. 2:16 So inside the main listings folder here, we're going to create a new file called urls.py, ( 2:12 create urls.py in listings and go to listings/urls.py). this is going to be similar to what we did with pages/urls.py, so I'm actually going to just copy that and bring that over to the new one here. So we want to import path.

# ----------------------------------Section 6: Models, Migrations & Admin-------------------------------------

# Install Postgres & pgAdmin - in Word


#Django Postgres Setup & Migrate -00:00  now to use postgres, we need to define a parameters in the settings file, but we also need to install a couple packages using PIP so that it can get drivers to connect to postgres. So make sure you're in your venv or whatever you call your virtual environment. And let's do a "pip install psycopg2" and then want to do that same thing, but, "pip install psycopg2-binary". so we want to install those two packages and to clear this up, and then we're going to go to Settings.py and go down to make sure let me make this smaller. We're going to go down to where it says database. (00:52 go to settings.py and go to databases)


# Planning Our Schemas - in Word.


# Create Listing Model - 00:00 We are going to create a listing model and a realtor model, then we will run a migration based on those models and this will create the tables for those models. :26 This is a Django "https://docs.djangoproject.com/en/3.2/topics/db/models/fields" this is the model field reference. When we setup our fields, we give them certain types. There is a whole bunch. CharField is going to be the most common type for cities, addresses and so on. (1:25 go to the listings/models.py)


# Realtor Model & Run MIgrations - 00:00 - now we need to create our realtor model (00:25 realtor/models.py)


# Create Superuser & Register Models With Admin - 00:00 Now we're going to start to work with the admin area, which, in my opinion, is one of the greatest features of Django, especially if you're a freelancer or someone that works by herself or just maybe with just a couple other people. You don't have this big giant team where they can create a custom admin area. It just gives you that right off the bat and you can customize it as you see fit. So if you make sure you have your server running and if you just go to localhost 8000 slash admin, it'll bring you right there. It's been here all along. Now, we don't currently have a way to log in. 


#Create Superuser & Register Models With Admin :42 So what we need to do is head over to our terminal. I'm using my vias code terminal and we need to create a super user if we do python manage dot pi help and take a look at. Let's see up at the top here, I believe under off, you see we have a create super user command. OK, so that's what we want to use. So let's go ahead and run. That will say "python manage.py createsuperuser". So for a username I'm going to use when am I going to use use "Alex". But you could use whatever you want. So email address. I'm going to say alex@squat.xyz, and then your password. So for my password, I'm just going to use one "1234". So it gives me just a message saying that my password sucks, should it? Should we bypass the validation anyway? And I'm just going to say yes. All right. So now we have a super user. So let's clear this out and let's go back to the admin area. And I'm going to put in mm log in and there we go. So now we are actually in the the administrator area now from here, without doing anything at all, we can manage our users in groups so we can assign groups and Django. so we can add groups with different permissions. We can also create and manage users. So here's our "Alex" user and notice that there's a staff status. So this is basically this just means that this user is an admin and they can actually log into this area. you'll have users that can log into the front end of your Web site but you you obviously don't want them to have access to this area. This is for staff only. (you can go in there and change staff status, superuser status, active status)
#Create Superuser & Register Models With Admin 3:17 Now, obviously, we want to be able to to to add listings. We want to be able to add realtors and stuff like that.(go to listings/admin.py)


# Media Folder & Adding Data - 00:00 We will be adding data, but before that we have to define some stuff for the media folder where the photos will get uploaded. (:27 go to btre/settings.py file and go to very bottom)


# Admin Logo & CSS - 00:00 We are goign to be changing up the logos for the admin area plus some other things. 00:59 what we want to do is create a folder in templates called admin, inside there create a file called "base_site.html". We then extend the admin template, and in there we can change blocks and such. (1:20 go to templates/admin/base_site.html to start editing the admin area). 


# Customize Admin Display Data - 00:00 We want to make the data displayed to us to be more informational This inlcudes listings. (00:29 go to listings/admin.py)


# ----------------------------------Section 7: View Methods, Display & Search-------------------------------------
# Pull Data From Listings Model - 00:00 Now, what we want to do is to have the models that we created for the databases, to actually be able to display the information that we have in our DB and loaded to the front end. To began doing this, we are going to began with going to the views.py in the listings app. (00:56 go to templates/listings/views.py)  

# Display Listings In Template - 00:00 As of now, we are outputting static html that isn't dynamic. We need to grab listings from our DB. Whats interesting is that there is six listings, as there are in our DB but there is no dynamic data. (00:36 go to templates/listings/listings.html to replace static variables with dyanmic variables)

# Pagination, Order & Filter - 00:00 Brad talks about pylinting issue that is something very minor and doesn't bother me, since these lessons are somewhat older. 1:00 he goes to paginator documentation https://docs.djangoproject.com/en/3.2/topics/pagination/. 1:10 You want to go down to paginator in a view. We want to add paginator, we pass in our listings and how many per page we want to use, you then you want to get the request for the page number you are on to keep track "request.GET.get('page')" and then we pass that into a variable that would hold "paginator.get_page(page)" (1:42 go to listings/view.py )

# Home & About Page Dynamic Content - 00:00 we need to take care of the realtors having dynamic view in the home page, along with other dynamic information we need to set up. (:53 go to pages/views.py)

# Single Listing Page - 00:00 (open up listings/views.py and then open and go to template/listings/listing.html)

# Search From Choices - 00:00 we want to shore up all the choices and make them mean something to Django. To do that we need to create a file called choices.py in Listings (00:52 go to the newly created listings/choices.py). 

# Search Form Filtering - 00:00 It is time to actually bring functionallity to these (00:50 go to listings/views.py)

# Preserving Form Input - 00:00 When we search something, we want it to stay in the form. Lets make this happen. (00:20 go to listings/views.py)


# ----------------------------------Section 9: Accounts & Authentication--------------------------------------------

# Accounts App & URLs - 00:00 We are now going to start on account functionality. To start on this, we need to create a new app, an account app. "python manage.py startapp accounts". Then we have an accounts folder that is started. Now, Django already has a user system in place. Which means that we don't have to create accounts or user model, we can just use the user table that is already in place. 2:18 if you go to pgAdmin and go to Servers/dbserver/databases/btredb/Schemas/public/tables and there is a table within there called "auth_user". 3:00 He goes tyhrough the fields that they automatically created and even "is_staff" is there, which is there to allow them to log into the back end or not.  The first step is to start creating the routes for the registration and login. First we want to create a folder in templates called accounts. Inside accounts we want to have a couple of files created, login.html, register.html and dashboard.html which will be part of accounts  (4:25 go to templates/accounts and input h1s to every single file in there.) after this we want to setup our routes. So go to accounts and create a file called "urls.py", since you have to make this file for Django (5:05 go to btre/settings.py).

# Register & Login Templates - 00:00 we are going to create the templates for login and register. (00:25 open and go to templates/accounts/login.html && templates/accounts/register.html )