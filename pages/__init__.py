#1:22 When we make a projectapp we have an __init__.py file and it's empty. We don't have to worry about it. Migration's is for any database. Migration's we create we're not going to have any migration's for this particular app, but we will in some of the other ones. Admin is if you want to like you want to show stuff in the admin area. We're not going to need to do that here in our listings app, We will, because we'll want to want to manage our listings from the admin area, but we won't touch this one. And then app.py, this shows you the class of the config. This will actually have to go in our settings file. Models, this is where we create our models. This particular app doesn't have a model, but for instance, "listings" will have like the the the title, the address, the number of bedrooms, all that stuff is going to be defined inside of a model. Then we have our tests if we want to run any tests and a Vieuxtemps PI file where we can create methods and we can actually link you URLs to those methods.