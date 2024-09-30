from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),  # Main page for ordering 
    path('order/', views.order, name='order'),  #Display an online order form 
    #path('confirmation/', views.confirmation, name='show_all'),  #Display a confirmation page after an order is placed 
]