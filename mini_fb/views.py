from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView 
#ListView is a generic class based view in Django that handles listing objects from a database 
# Create your views here.

class ShowAllView(ListView):
    '''Create a subclass of ListView to display all blog articles.'''
    model = Profile # retrieve objects of type Article from the database
    template_name = 'minifb/show_all.html'
    context_object_name = 'profiles' # how to find the data in the template file


