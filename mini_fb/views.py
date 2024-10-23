from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.views.generic import ListView, DetailView, CreateView
from .forms import CreateStatusMessageForm
from django.utils import timezone
import random
from django.urls import reverse
#ListView is a generic class based view in Django that handles listing objects from a database 
# Create your views here.

class ShowAllView(ListView):
    '''Create a subclass of ListView to display all blog articles.'''
    model = Profile # retrieve objects of type Article from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file

class ShowProfilePageView(DetailView):
    '''Show the profile for one article using DetailView'''
    model = Profile #this is the model we want to grab an instance from 
    template_name = 'mini_fb/show_profile.html' #this is the profile we delegate the work to
    context_object_name = 'profile' #we are passing one profile as context

    #pick one profile to show at random 
    ''' Django uses this method to fetch the object based on the 'pk' ''' 
    def get_object(self):
        return super().get_object()  # Automatically fetches the Profile by 'pk'
    
class CreateStatusMessageView(CreateView):
    '''A view to create a new status message and save it to the database'''
    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def form_valid(self, form):
        # Get the profile object based on the primary key passed in the URL
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.instance.profile = profile  # Associate the status message with the profile
        form.instance.timestamp = timezone.now()  # Set the current time as the timestamp
        return super().form_valid(form)  # Save the form and redirect

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the profile to the context so it can be used in the template
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        # Redirect to the profile page after successfully creating a status message
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})
