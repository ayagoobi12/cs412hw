from django.shortcuts import render
import random

# Create your views here.
QUOTES = [
    "I've practiced so much that it's just ingrained in me. But it's important to have fun, too. Sometimes I even smile on the court.",
    "Tennis can be a very frustrating sport, but you have to stay calm and composed if you want to succeed.",
    "I fear no one, but respect everyone.",
    "I always believe if you're stuck in a hole and maybe things aren't going well you will come out stronger. Everything in life is this way.",
    "You have to put in the hours because there’s always something which you can improve.",
    "Sometimes you have to accept that a guy played better on the day than you.",
    "I’m a very positive thinker, and I think that is what helps me the most in difficult moments.",
    "The serve, I think, is the most important shot in the game. It’s the only shot you have full control over."
]
IMAGES = [
    "https://cdn.britannica.com/22/188722-050-BB193EA3/Roger-Federer-US-Open-2007.jpg",
    "https://media.gq.com/photos/596c23a0ae316b7975876777/16:9/w_2560%2Cc_limit/gq-federer.jpg",
    "https://cdn.britannica.com/23/188723-050-332EE886/Roger-Federer-US-Open-2014.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/a5/Roger_Federer_Wimbledon_2012.jpg",
    "https://static01.nyt.com/images/2018/06/24/sports/24federer1/merlin_139929545_63473b87-3626-453b-8229-32d2035f0a29-superJumbo.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/3b/Roger_Federer_2011.jpg",
    "https://media.vanityfair.com/photos/5d3052837c978b00088372d8/master/w_2560%2Cc_limit/roger-federer-2019-embed.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/50/Roger_Federer_Madrid_Open_2019.jpg"
]

def quote(request):
    """"Main page view which selects a random quote and and image to display"""
    selected_quote = random.choice(QUOTES)
    selected_image = random.choice(IMAGES)
    
    #pass the selected quote and image to the template as context variables 
    #this is a dictionary that holds data you want to pass from your view to the template

    context = {
        'quote': selected_quote,
        'image': selected_image
    }
    #this function is provided by Django and is used to combine the template (in this case 'quote.html') and return an HTTP response. 
    return render(request, 'quote.html', context)

def home(request):
    """"Main page view which selects a random quote and and image to display"""
    selected_quote = random.choice(QUOTES)
    selected_image = random.choice(IMAGES)
    
    #pass the selected quote and image to the template as context variables 
    #this is a dictionary that holds data you want to pass from your view to the template

    context = {
        'quote': selected_quote,
        'image': selected_image
    }
    #this function is provided by Django and is used to combine the template (in this case 'quote.html') and return an HTTP response. 
    return render(request, 'quotes/quote.html', context)

def show_all(request):
    """View to display all quotes and images"""
    # Pass all quotes and images to the template
    context = {
        'quotes': QUOTES,
        'images': IMAGES
    }
    return render(request, 'quotes/show_all.html', context)

def about(request):
    """About page view that displays information about Roger Federer and the app creator."""
    # Add context data containing information about Roger Federer and the app creator
    context = {
        'person_name': 'Roger Federer',
        'biography': """
            Roger Federer is a Swiss professional tennis player who is widely regarded as one of the 
            greatest tennis players of all time. He has won 20 Grand Slam singles titles and has spent a 
            record total of 310 weeks as the world No. 1 in the ATP rankings.
        """,
        'app_creator': 'Aidan Yagoobi', 
        'creator_info': 'A passionate developer learning Django!',
    }
    
    return render(request, 'quotes/about.html', context)