from django.db import models
from datetime import datetime
#Realtor Model & Run MIgrations 00:25 Here we create our Realtor class and extend the models.Model to start creating our models from our DB. 
class Realtor(models.Model):
#Realtor Model & Run MIgrations:30 - 1:12 we will input the fields for the Realtors 
    name = models.CharField(max_length = 200)
    #Realtor Model & Run MIgrations 1:12 lets set this to the same thing as we did witht he other photo
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    description = models.TextField(blank = True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.name
    
# Realtor Model & Run MIgrations 3:47 So now that we have the realtors and listings model's done now, we want to get this stuff into the database right now, it's not in the database. just because we created the models, it doesn't mean that those tables are created and you'll see there's no new tables for listings or realtors. So we need to create a migration or make a migration and then run it. 4:32 to do this we want to run the code, in the venv, "python manage.py makemigrations", this is going to create a file and not actually create a database. (5:17 he runs this and gets abunch of errors) in order to run this, we need to have a dependency called "pillow", thats because in order for us to actually use ImageField we need an install called "Pillow", once you do that(5:36 run pip install Pillow), you can run the migrations. 5:44  notice that it's not only did it do Listing's now, we could have done and I actually meant to do "python manage.py makemigrations listings", but it doesn't matter since realtors is a foreign key on listings, they both would have ran. If we do just the "python manage.py makemigrations" it would run both of them. 
# Realtor Model & Run MIgrations 6:08 And it's created a file called "0001_initial.py" inside both migrations folders.  now if we take a look at these files, this is what migrations look like and they include this operations list with migrations create model has a name and then it has all the fields. so this is basically what's going to be read into the database. There's actually a command that we can run to check out what the query would look like. So if we do: "python manage.py sqlmigrate listings 0001",this isn't something you have to do. I'm just showing you it's an option. Once you enter this, it will show the SQL command for this, it wont run it, just show it. 
# Realtor Model & Run MIgrations 7:56 lets get the migration ready, to do this, lets input "python manage.py migrate". we get two "ok"s from realtors and listings.  so now that that specific command actually changed the database, added the table. (8:16 So let's take a look. he looks at the tables in the pgAdmin)