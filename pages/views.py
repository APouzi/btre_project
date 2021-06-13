from listings.views import listing
from django.shortcuts import render
from django.http import HttpResponse
#Search From Choices - 2:05 since its from listings.py we want to do "listings.choices"
#Search From Choices - 9:59 copy and paste the imports from listings.choices that we had in the pages/views.py
from listings.choices import price_choices, bedroom_choices, state_choices
#Creating the Pages & Base Layout - 6:25 Lets create the function for the urls.py, after that import HttpResponse from the django http package. For now we ware just going to be using HttpResponse for example. @7:40 This isn't going to work because we still need to take the urls.py file and go to the other urls.py file and make some changes there (8:10 Go to urls.py in BTRE)

#Home & About Page Dynamic Content - 00:59 Right now it's very simple and also open up templates/pages/index.html. We are going to do the same exact thing we did with the listings page but no listings and just three listings. Even though we are inside the pages app, we can get any model we want. So that means we should bring in the listings model because that is where the DB data is. So we should importa that.
from listings.models import Listing
from realtors.models import Realtor


#Pages Templates & Base Layout - @2:41 we want to make sure that we have the render instead of the HttpResponse that we had, so replace that with the return of the render function/method and pass in the request and route. Create that "about" function for the about path. (3:40 he goes to urls.py and then saves again to refresh, nothing too important. He says to always make sure we are in the virtual env)(4:30 he is done checking out the sites working and goes to urls.py)
def index(request):
#Home & About Page Dynamic Content - 1:44 we are going to be creating a variable called listings and setting it to the Listing model that we imported in. We are going to be ordering the listings by list_date and it's going to be desending. On top of that we are going to be making sure the unpublished ones are not there and we want to limit this to only 3 listings, so we will be using "[:3]".
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
#Home & About Page Dynamic Content - 2:33 we then have to create a context variable, like the listings view.py. 2:55 now we're passing it into the index.html, we just need to receive it and loop through them and display the dynamic data just like we did with the listings,.html file. (3:10 go to templates/pages/index.html )
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
#Search From Choices - 2:24 we want to bring these imports into the context dictionary so we an pass them off in the return ()
    }
    return render(request, 'pages/index.html', context)


#Home & About Page Dynamic Content -10:21 We want to do the samething but for the realtor model so we have to import the Realtors "from realtors.models import Realtor" 
def about(request):
#Home & About Page Dynamic Content -10:45 Here we create a variable for us to set it to the object model of realtors. We also want to order them by seniority.
    realtors = Realtor.objects.order_by('-hire_date')
#Home & About Page Dynamic Content -11:41 Since we set kyle brown to mvp, we want to grab a group, just in case there is more than one.
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)
#Home & About Page Dynamic Content -12:40 now we have to set this to a dictionary, we will be setting realtors to realtors. Also mvp_realtors too, pass this into to the return (13:08 go to "templates/pages/about.html")
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors

    }

    return render(request, 'pages/about.html', context)

