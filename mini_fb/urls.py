## Create app-specific URL:
# blog/urls.py
from django.urls import path
from .views import ShowAllView, ShowProfilePageView, CreateStatusMessageView # our view class definition 
urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllView.as_view(), name='base'), # generic class-based view
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'), #this link has a name which allows us to access it, this url has a name which we can use to grab the url itself by using the url tag in the template
     path('profile/<int:pk>/create_status/', CreateStatusMessageView.as_view(), name='create_status')
]