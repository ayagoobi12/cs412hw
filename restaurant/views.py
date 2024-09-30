from django.shortcuts import render
import random
import time
from datetime import datetime, timedelta

# Create your views here.
def base(request):
    """Main page view for the basic information about the restauraunt"""
    name = "Paristanbul"
    location = "116 Rue du Faubourg Saint-Martin, 75010 Paris, France"
    photo = "https://upload.wikimedia.org/wikipedia/commons/f/fb/Paristanbul.jpg"
    hours = [
        {"day": "Monday", "open": "9:00 AM", "close": "5:00 PM"},
        {"day": "Tuesday", "open": "9:00 AM", "close": "5:00 PM"},
        {"day": "Wednesday", "open": "9:00 AM", "close": "5:00 PM"},
        {"day": "Thursday", "open": "9:00 AM", "close": "5:00 PM"},
        {"day": "Friday", "open": "9:00 AM", "close": "5:00 PM"},
        {"day": "Saturday", "open": "10:00 AM", "close": "4:00 PM"},
        {"day": "Sunday", "open": "Closed", "close": ""}
    ]

    context = {
        'name': name,
        'location': location,
        'hours': hours,
        'photo': photo,
    }

    return render(request, 'restaurant/base.html', context)


def order(request):
    """View to handle the ordering of items"""
    menu_items = [
        {"item": "Chicken Kebab Skewer", "price": "$7.99"},
        {"item": "Chicken Kebab Plate", "price": "$12.99"},
        {"item": "Lamb Kebab Skewer", "price": "$8.99"},
        {"item": "Lamb Kebab Plate", "price": "$13.99"},
        {"item": "Loaded Fries", "price": "$5.99"},
        {"item": "Falafel Wrap", "price": "$6.50"},
        {"item": "Beef Shawarma Wrap", "price": "$8.50"},
        {"item": "Hummus and Pita", "price": "$4.99"},
        {"item": "Grilled Veggie Plate", "price": "$7.99"},
        {"item": "Greek Salad", "price": "$6.99"},
        {"item": "Baklava", "price": "$3.99"}
    ]

    daily_special_items = [
        {"item": "Spicy Lamb Meatballs", "price": "$9.50"},
        {"item": "Chicken Shawarma Platter", "price": "$11.99"},
        {"item": "Vegetarian Sampler", "price": "$10.50"},
        {"item": "Garlic Fries", "price": "$6.50"},
        {"item": "Beef Kofta Plate", "price": "$13.50"},
        {"item": "Couscous Salad", "price": "$7.50"}
    ]
    selected_daily_special = random.choice(daily_special_items)

    if request.method == "POST": #if the user submitted the form, we need to handle to form submission 

        #Generate the time submission occurred at and find the time it will be finished at 
        current_time = datetime.now()

        random_minutes = random.randint(30, 60)

        # Add 25 minutes using timedelta
        new_time = current_time + timedelta(minutes=random_minutes)

        # Format the result
        formatted_new_time = new_time.strftime("%Y-%m-%d %H:%M:%S")

        # Handle the form submission
        menu_items_selected = request.POST.getlist('menu_items') #grab all the menu items 
        daily_special_selected = request.POST.get('daily_special') #only one daily_special, not a list 
        extras_selected = request.POST.getlist('extras') #grab all the extras 
        special_instructions = request.POST.get('special_instructions') 
        customer_name = request.POST.get('name')
        customer_phone = request.POST.get('phone')
        customer_email = request.POST.get('email')

        # Now you can process this data (save it to the database, send an email, etc.)
        # For this example, we'll just print it or save it in a variable
        order_summary = {
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'customer_email': customer_email,
            'menu_items_selected': menu_items_selected,
            'daily_special_selected': daily_special_selected,
            'extras_selected': extras_selected,
            'special_instructions': special_instructions,
            'time': formatted_new_time
        }

         # Redirect to a confirmation page after form submission
        return render(request, 'restaurant/confirmation.html', {'order_summary': order_summary})

    #If it's a get request, and no form submission, simply display the context values
    context = {
        "menu": menu_items, 
        "daily_special": selected_daily_special,
    }
    return render(request, 'restaurant/order.html', context)

