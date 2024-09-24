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
    "https://i.cbc.ca/1.6583766.1692147119!/fileImage/httpImage/federer-roger-091522.jpg",
    "https://assets.vogue.com/photos/66a6fe133fae08117a60129f/master/w_2560%2Cc_limit/GettyImages-161555765_SCALED_LUC.jpg",
    "https://media.npr.org/assets/img/2022/09/15/gettyimages-1233248343_custom-c80c2a9cc7a4ae6e3de994ee9d146a8be2e61afe.jpg?s=1100&c=50&f=jpeg"
    "https://images.tennis.com/image/private/t_q-best/tenniscom-prd/trnjjhiqerwljw95vbmw.jpg"

   
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

def base(request):
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
    return render(request, 'quotes/base.html', context)

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