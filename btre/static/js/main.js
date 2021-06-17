const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//Message Alerts - 11:19 we want to use alitte jquery to do a fade out. We are going to use a JS function called "fadeout". insdie there we have the message and have it slowly fade out, have this all take 3 seconds. Once we do this, sicne this is in the static folder, we want to run a "collectstatic" because this is in the btre static folder and we want it to be in the main static folder. So in the terminal run a "python manage.py collecstatic" in venv obvisouly. Now, it will probably have an issue if you don't clear you cache. END OF VIDEO
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);

