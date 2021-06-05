
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dy86ybpww^fkz)w@!63t#s7c6vy0lg_(_pz!g3=_19-fl33e3a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Creating The Pages App -  2:30 We are going to put "pages.apps.PagesConfig" into installed apps. He got this from "apps.py" in pages. @3:40ish he talks about how autopep3 might come up when you save this and you should just install it in the virtual environment. @4:10 close that up and now he wants to create a urls.py file for the pages app. <create file called "urls.py" in the pages folder and go to it)
# Application definition
INSTALLED_APPS = [ 
    'pages.apps.PagesConfig',
#Listings URLS & Templates - 5:36 Here we will be adding the listings and realtors definitions for the installed apps. 5:44 now we need to create our views methods that we had in our listings/urls.py (5:55 go to listings/views.py to create methods). Note we cannot do a "python manage.py startapp realtors" or whatever app if we already inputted the defition of it in here.
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btre.urls'

#Pages Templates & Base Layout - 00:39 you want to go down to here, with all the key value pairs and it has the "DIRS". Which is where we want go. 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#Pages Templates & Base Layout - 00:47 we want to tell templates where to look. Brad says he puts his templates in the root and not in the pages or anything and to let it know that we are going to say "os.path.join(BASE_DIR, 'templates')" BASE_DIR means base directory and the folder name we want to use is "templates".
#@1:20 then we want to go into the root of the project and create a folder called "Templates" and go there. He also talks about how it's up to you how to organize templates but he likes to categorize them by application and has a folder within there for that. @1:40 create a folder within Templates called page, we then created an index and about html file inside that folder. (2:06 go to Templates.Pages folder and input the <h1> tags in the html files) (2:15 go to pages/urls.py)
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 1:10 First we want to change "django.db.backends.sqlite3" and for the name, we want to get rid of what was there before and input "BASE_DIR / 'db.sqlite3'"". Then we want to add in the USER, PASSWORD, and HOST in there since its not there already. 
# 2:10 as far as the messages that say "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions" we saw this a long time ago when we first started the server for localhost, basically we have some unappointed migrations and immigration is a file that that tells the database what to do basically is as far as setting up tables and data columns and data types of each for each column and stuff like that. And Django has default migrations for things like the admin area for authentication. There's going to be users that have to do with the admin area that that stuff is all set up. Those migration files are set up. They just haven't been run and put into the database. So what we want to do now is, is basically run those migrations. And once we do that, we won't see this error anymore. 3:03 So lets stop the server, Now, to basically to to migrate, we're going to create our own migrations for like the listing's and the realtors and stuff like that, but to run the current migrations that are already ready like those 15 that were in that message, we just want to say "python manage.py migrate". now, if something isn't right with our database, we're going to see an error here. So let's just try it out. 4:04 Now, if you go to pgAdmin then go to severs> dbserver> Datab ases> btredb> Schemas> Tables and you will see all the interesting. This now means that we know postgres is interacting with our application. Also those errors are now gone, because the mirgations have been activated, which means we can create our own models and connect them to our table. END OF VIDEO

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static Files & Paths - 2:36 we now have a static url that is set to static, there already. But we want to add two other things here. One is going to be the STATIC_ROOT. The idea of this is when you deploy your application, you run a command called Collect Static and it goes into all of your apps. And if it has a static folder, it takes everything out and puts it into a root static folder. So that's what we're defining here. Just like we did with the templates, instead we input in "static", we use the "os.path.join(BASE_DIR, 'static')""

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# 3:11 We input the second one, "STATICFILES_DIRS". We want to set the location of the static folder we just created, which is in this BTR folder. So the way that we can do that is OS.path.join(BASE_DIR, 'btre/static') Base Dir, and then we want btre/static.(3:53 he then inputs the command "python manage.py collectstatic", what this does is find any static folders we have and create one into whatever we define as the static root. You can call this anything. 4:21 he runs it, you can see that it actually created a static folder in our route, which has not only the stuff that we put in the our root, but also the static admin CSS and stuff files. So when we deploy, this is actually where it looks for everything, including the admin costs and all that stuff. So once we put this on our server, we want to run that command. Now, one thing we don't want is to push this to our repository. ) 4:52 Now, one thing we don't want is to push this to our repository. So we're going to go to our .gitignore and we're actually going to add "/static". then another thing that I forgot to do is to add a slash in front of "media" because I only want the root static and media to to not be pushed to the repository (end of video).
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media Foilder Settings
# Media Folder & Adding Data - 40 we need to set some things, so we will put "Media Folder Settings". What we want to define is a MEDIA_ROOT. We want this to be in a root folder called Media. So we want to pass in "BASE_DIR" as first parameter and the folder we want to call it. 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 1:15 then we want to set our MEDIA_URL to "/media/" just like we did with the static url. (1:37 go to btre/urls.py to change one more thing)
MEDIA_URL = '/media/'