## formdata/urls.py 
## Define the urls for this app 

from django.urls import path 
from django.conf import settings 
from . import views 

#Define a list of valid url patterns: 
urlpatterns = [
    path(r'', views.show_form, name="show_form"),
]