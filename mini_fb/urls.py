## Create app-specific URL:
# blog/urls.py
from django.urls import path
from .views import ShowAllView # our view class definition 
urlpatterns = [
    # map the URL (empty string) to the view
    path('', ShowAllView.as_view(), name='base'), # generic class-based view
]