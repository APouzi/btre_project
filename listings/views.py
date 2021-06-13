from typing import List
from django.shortcuts import get_object_or_404, render
#Pagination, Order & Filter - 3:24 this is where we are going to be importing a couple of things aside from the paginator itself.  
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#Listings URLS & Templates - 6:03 we create a index method and that is going to be the main listings page. What he is going by is the urls.py so create three methods in total for listings, listing, and search.  (7:11 for each html in listing, put in an h1 for placeholders, then check on server to see if okay) 10:10 Extend the base to the layouts(10:14 go to listings, listing and search, extend the base.html and input block content temple tags). 11:14 Now we are going to get the static stuff for listings, so we go to notepad++ and go to theme/dist to go and get the html. Below navbar and above footer. Copy and paste into each of the files.  (12:48 go to listings.html) 
from listings.choices import price_choices, bedroom_choices, state_choices 
#Search From Choices -  10:00 We want import the same dictionaries from choices in listings just like we did in pages/views.py and but unlike there we take off "listings" from "listings.choices".


from .models import Listing
#Pull Data From Listings Model - 1:05  index is what we're looking at. It's displaying the listings.html and if you forget why this is displaying, it's because in our urls.py, we have just /listings and urls.py represents /listings and it's calling the index method inside the view file. 1:27 So the idea here is we fetch our listings using our model and then we inserted into our template and then we can just simply loop through and output the listings that are in the database. In order to do that, we need to bring in our listing model, so "from .models import Listing". 2:12 Brad shows an example of how you can pass in values dynamically via "{}" and then he goes to listings/listings.html" and puts a place for it to be outputted with the "{{}}". 

def index(request):
#Pull Data From Listings Model - 3:20 We want to pass in our listing, to do that we need to fetch it from our DB. To do that, he inputed "listings = Listing.objects.all()"
  # listings = Listing.objects.all()


#Pagination, Order & Filter - 16:20 Instead of doing just "all()" we will be doing an orderby function and pass in list_date but we want it decending, so put in a minus "-list_date". Lastly we want to make sure that unpublished titles are not inside of our listings, so we add on a filter function and pass in is_published = True. END OF VIDEO
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
#Pagination, Order & Filter - 1:55 Here is where we will be adding a paginator, in the index under listings. For now, we will do 3 per page, but we want to do 6 per page after. The pagination will go away if we turn these to six because we only have six results and that means it all fits on one page.
  paginator = Paginator(listings, 6)
#Pagination, Order & Filter - 2:20 Here is where we will be getting our page by creating the variable and setting it to request.GET.get and the url parameter we are looking for, which is page
  page = request.GET.get('page')
#Pagination, Order & Filter - 2:40 Now we are going to get paged_listings set up. After that we want to change 'listings': listings to 'listings' : paged_listings because we don't want to directly use that listings anymore and use the paginated version.3:20 We are getting an error saying that paginator doesn't exist, that is because we need to bring it in and import it.
  paged_listings = paginator.get_page(page)
#Pagination, Order & Filter - 3:54 this takes care of fetching the data but not displaying it in the actual view. 4:00 if we go back to the documentation, it shows us how to do that but instead they are using contacts but we are using listings. We can check to see if there is a previous page, what that previous page number is and a link going to it. 4:17 We would go to the href/URL and then the parameter of page equals and then the previous page number down here, we can see if there is a next and then we can make a link going to the next page number. You can simply copy this and make it look like crap, but instead we are going to be using bootstrap pagination looks at 4:39 in video. WATCH THIS PORTION OF VIDEO AS HE EXPLAINS THE PAGINATION OF BOOTSTRAP AND IT'S COMPONENETS AND THEN TYPE IT IN. (5:25 Go to template/listings.html)




#Pull Data From Listings Model - 2:50 usually we don't pass in the dictionary as the second value, what we do is create a variable with the dictionary in there and pass that in there. 3:05 So what we would do is pass in this context here, into the second parameter. 
  context = {
#Pull Data From Listings Model - 3:50 we change this to 'listings' for the key. Now, he goes into the fact that we have an issue with "listings = Listing.objects.all()" unless we do a "pip install pylint-django". Just doing that isn't going to get rid of the error. This wouldn't have actually given you any issues when functioning but in the editor it's a thing. 5:57 recap of what we did. Listing.objects.all() is getting all the listings without any need of querying. Then we pass this into the dictionary we made called "context". This context is passed into the return, as a 3rd paramter. (6:13 templates/listings/listings.html)
    # 'listings': listings
    'listings' : paged_listings
  }

  return render(request, 'listings/listings.html', context)


#Single Listing Page - 2:49 Here we want to start making our single listings into dynamic pages. To do this, we need to reach into the model and grab that particular data. Since we already brought in the listing method to the file, we want to start a variable called listing. Instead of getting the object the usual way, we are going to be using get_object_or_404(). This will essentially show a 404 page if nothing is retrieved. 3:31 We want to pass in the model and also the primary key to listing_id, this primary_key is passed in through the listing function itself and that is passed into the get_object_or_404 function. Though that one actually comes from the urls.py in listing . Then set up the context dictionary to pass through the return of the render. Make sure to import in the get_object_or_404 from django.shortcuts. 5:05 Now that is done, we should be able to access the listing data within the template because we passed it in with the return that includes "listings/listing.html". (5:21 go to listing.html)
def listing(request, listing_id):

  listing = get_object_or_404(Listing, pk = listing_id)
  context = {
    'listing' : listing
  }

  return render(request, 'listings/listing.html', context)



def search(request):
#Search Form Filtering - 00:55 We are going to start, at the top, a queryset_list as brad calls it. This one alone is just going to get all the listings. Now we need to add filters to the search. 1:45 The first thing we need to get done, is update the context dictionary and pass in the listings as a queryset_list. 
  queryset_list = Listing.objects.order_by('-list_date')
#Search Form Filtering - 4:29 We first start with commenting all the fields that we want to filter, 
  # # Keywords
#Search Form Filtering - 4:45 when you make a request with this form, it's a get request and you can actually test to see if it exists. 4:53 if it does, we want to do a "keywords = request.GET['keywords']", then we want to do another if statement "if keywords" the reason we want to do that, is to check that if it is an empty string, if this succeeds we want to set another filter on it that asks if the keywords are contained in the descrption field, in our model. 6:01 If we do something that isn't an exact match, more like an actual search within something that is a pool of words like a description. We want to put an DOUBLE underscore "__" and then we do an "icontains"
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # # City
  # if 'city' in request.GET:
  #   city = request.GET['city']
  #   if city:
  #     queryset_list = queryset_list.filter(city__iexact=city)

  # # State
  # if 'state' in request.GET:
  #   state = request.GET['state']
  #   if state:
  #     queryset_list = queryset_list.filter(state__iexact=state)

  # # Bedrooms
  # if 'bedrooms' in request.GET:
  #   bedrooms = request.GET['bedrooms']
  #   if bedrooms:
  #     queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # # Price
  # if 'price' in request.GET:
  #   price = request.GET['price']
  #   if price:
  #     queryset_list = queryset_list.filter(price__lte=price)


#Search From Choices - 10:20 We are also going to be using the choices that we are importing just like we did in the views.py.  dont forget to pass in the context into the return. (10:50 go to template/listings/search.html)
  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
#Search Form Filtering - 1:45 pass in listings as queryset_list, 2:06 so now lets just make the template load the unfiltered queryset_list to do this we need to copy what we have in listings.html into search html (2:18 go to templates/listings/listings.html)
    'listings': queryset_list,
    # 'values': request.GET
  }


  
#Search From Choices - 6:40 if we submit and you see that what happens here is the return is just "listings/search.html" which returns a simple template. 7:00 If we were to put values in search fields, we actually see those values inside the url bar. 7:17 lets add the markup to the search page, get that from the btre_resources with the notepad++ editor, copy only contents needed, not tamplates. (go to templates/listings/search.html)
  return render(request, 'listings/search.html', context)
