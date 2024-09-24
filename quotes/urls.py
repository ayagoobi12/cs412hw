from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'), # / route
    path('quote/', views.quote, name='quote'), #/quote route
    path('show_all/', views.show_all, name='show_all'), 
    path('about/', views.about, name='about'),
]