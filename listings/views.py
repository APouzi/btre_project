from django.shortcuts import render
# Listings URLS & Templates - 6:03 we create a index method and that is going to be the main listings page. What he is going by is the urls.py so create three methods in total for listings, listing, and search.  (7:11 for each html in listing, put in an h1 for placeholders, then check on server to see if okay) 10:10 Extend the base to the layouts(10:14 go to listings, listing and search, extend the base.html and input block content temple tags). 11:14 Now we are going to get the static stuff for listings, so we go to notepad++ and go to theme/dist to go and get the html. Below navbar and above footer. Copy and paste into each of the files.  (12:48 go to listings.html) 
def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
