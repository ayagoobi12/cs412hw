from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),  # Home page for quotes
    path('quote/', views.quote, name='quote'),  # Display one random quote
    path('show_all/', views.show_all, name='show_all'),  # Display all quotes
    path('about/', views.about, name='about'),  # About page
]