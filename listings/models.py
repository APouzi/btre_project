from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create Listing Model - 1:27 Every time you create an app, a models.py is created with it. The way we define a model is with a class, we do a singular version of the app "listing". What we pass in is models.Model, so basically we are extending the core model is which gives us a whole lot of stuff to work with. Within this class, we create all of our properties. 
class Listing(models.Model):
#  Create Listing Model - 2:05 So the first one I'm going to create is the realtor and this is going to be the most difficult one, because this is going to be part of another table. So it's going to be the foreign key of another table so that we can form a relationship between realtors and listings. So we're going to set this to models.foreign key and this is going to take in the name of the other model that we're relating, which is going to be realtor. Then it takes a second parameter of what to do when you delete, because if you think about it, if you have a realtor attached to a listing and you delete the realtor, what what do you want to happen to the listing? Should the listing delete? In some cases you may want it to. I don't. So I'm going to actually set this equal to models.DO_NOTHING.
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
# Create Listing Model - 3:05 The second one is going to be the title, with parameter of max_length
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
# Create Listing Model - 4:25 because description is longer we want to do textfield and we don't need a max field with text field, we also want to pass in blank = true, this means that this field is optional.
    description = models.TextField(max_length = 200)
# Create Listing Model - 5:10 We will do price and we don't need a parameter for that.  
    price = models.IntegerField()
    bedrooms = models.IntegerField()
# Create Listing Model - 6:07 we will be making this into the decimal field to represent half bathrooms. We will put max_digits of two so the first number can only be two digits, cause no house has 100 bathrooms and decimal places is going to just be one. 
    bathroom = models.DecimalField(max_digits=2, decimal_places= 1)
# Create Listing Model - 6:51 garage but with default of 0.  
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
# Create Listing Model - 7:56 So now we want to we want to do the photos now in the schema that we created in the last video, I said it was a string, but that's that's in the actual database with with Django. We have different types of fields, like we have an image field. So that's what we want to use for the photos or the images but in the database itself, it'll be a string. 2nd paramater is  is where we want to we want to define where the where these get uploaded to. Now there's something called a media folder in Django and we're going to set that up in anything that we upload as far as images or files in the admin area is going to go into that media folder. But what we want to do here is define the folder that we want inside of that media folder. So we want to say upload, underscore to and you'll see all this in the documentation. If you want to look further into this stuff, we're going to say upload_to and let's call the folder "photos". Now, we could leave it like that, but I want each photo to go into a folder structure of the date. So basically, like the year, the month and the day and you'll see what I mean once we actually upload a file. But the way that we do this is we use the date format: photos/%Y/%m/%d/, notice the difference in capitalization of the letters. So that's the this is the location inside the media folder that this this field should go to. Do this for the other photos. Each of the other photos are going to be thumbnails that open with lightbox, the differewnce with these six images is that the images are going to be optional, so we use a "blank = True". N0TE about Image field, we need the dependency called "pillow" to run ImageField
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
# Create Listing Model - 10:51 Now that the photos are taken care of, lets get the is_published taken care of, with default of true
    is_published = models.BooleanField(default=True)
# Create Listing Model - 11:05 we also want the publishign date and to get that we have to import the date/time package to get the current date and time. So we input "from datetime import datetime", then put "datetime.now" to get the time of the listing at the time posted, and we also want that to be able to not have a listing date if needed, so blank = True.
    list_date = models.DateTimeField(default=datetime.now, blank=True)

#Create Listing Model - 2:06 As far as fields now with our with our admin area, when we have I mean, I haven't even showed you the admin area because there's we have no models yet to really show you anything. But we're going to have a table that's going to display each listing and we need to pick a field to be kind of the main field to to be displayed. And what I would suggest here is the title to be the main field to display. So to display whatever main field we want to display, we want to do the following(N0TE: make sure this function is inside the class):
    def __str__(self):
        return self.title 

#Create Listing Model - 13:00 Last thing we need to do, is to take care of the Realtor error we get on line 7 or the very top. To do that we need to import Realtor from realtor app.  we can just access any other app we want by just saying the name of it and then we can get its models by saying realtors.models and then we want to import the name of the model, which is realtor. We still need to create that in models. END OF VIDEO.
