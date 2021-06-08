from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices
# Listings URLS & Templates - 6:03 we create a index method and that is going to be the main listings page. What he is going by is the urls.py so create three methods in total for listings, listing, and search.  (7:11 for each html in listing, put in an h1 for placeholders, then check on server to see if okay) 10:10 Extend the base to the layouts(10:14 go to listings, listing and search, extend the base.html and input block content temple tags). 11:14 Now we are going to get the static stuff for listings, so we go to notepad++ and go to theme/dist to go and get the html. Below navbar and above footer. Copy and paste into each of the files.  (12:48 go to listings.html) 


from .models import Listing
#Pull Data From Listings Model - 1:05  index is what we're looking at. It's displaying the listings.html and if you forget why this is displaying, it's because in our urls.py, we have just /listings and urls.py represents /listings and it's calling the index method inside the view file. 1:27 So the idea here is we fetch our listings using our model and then we inserted into our template and then we can just simply loop through and output the listings that are in the database. In order to do that, we need to bring in our listing model, so "from .models import Listing". 2:12 Brad shows an example of how you can pass in values dynamically via "{}" and then he goes to listings/listings.html" and puts a place for it to be outputted with the "{{}}". 

def index(request):
#Pull Data From Listings Model - 3:20 We want to pass in our listing, to do that we need to fetch it from our DB. To do that, he inputed "listings = Listing.objects.all()" Now, when we first started this, we 
  listings = Listing.objects.all()
  # listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  # paginator = Paginator(listings, 6)
  # page = request.GET.get('page')
  # paged_listings = paginator.get_page(page)
#Pull Data From Listings Model - 2:50 usually we don't pass in the dictionary as the second value, what we do is create a variable with the dictionary in there and pass that in there. 3:05 So what we would do is pass in this context here, into the second parameter. 
  context = {
#Pull Data From Listings Model - 3:50 we change this to 'listings' for the key. Now, he goes into the fact that we have an issue with "listings = Listing.objects.all()" unless we do a "pip install pylint-django". Just doing that isn't going to get rid of the error. This wouldn't have actually given you any issues when functioning but in the editor it's a thing. 5:57 recap of what we did. Listing.objects.all() is getting all the listings without any need of querying. Then we pass this into the dictionary we made called "context". This context is passed into the return, as a 3rd paramter. (6:13 templates/listings/listings.html)
    'listings': listings
  }

  return render(request, 'listings/listings.html', context)



def listing(request):


  return render(request, 'listings/listing.html')



def search(request):
  # queryset_list = Listing.objects.order_by('-list_date')

  # # Keywords
  # if 'keywords' in request.GET:
  #   keywords = request.GET['keywords']
  #   if keywords:
  #     queryset_list = queryset_list.filter(description__icontains=keywords)

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

  # context = {
  #   'state_choices': state_choices,
  #   'bedroom_choices': bedroom_choices,
  #   'price_choices': price_choices,
  #   'listings': queryset_list,
  #   'values': request.GET
  # }

  return render(request, 'listings/search.html')
