"""
URL configurations for the final_project app.
Maps URL paths to corresponding views for Airlines (CRUD), flights search, 
flight list, and passenger list.
"""

from django.urls import path
from .views import (
    AirlineListView, AirlineDetailView, AirlineCreateView, 
    AirlineUpdateView, AirlineDeleteView, flight_search_view,
    FlightListView, PassengerListView
)

app_name = 'final_project'

urlpatterns = [
    # Airline CRUD
    path('airlines/', AirlineListView.as_view(), name='airline_list'),
    path('airlines/create/', AirlineCreateView.as_view(), name='airline_create'),
    path('airlines/<int:pk>/', AirlineDetailView.as_view(), name='airline_detail'),
    path('airlines/<int:pk>/update/', AirlineUpdateView.as_view(), name='airline_update'),
    path('airlines/<int:pk>/delete/', AirlineDeleteView.as_view(), name='airline_delete'),

    # Flight search and listing
    path('flights/search/', flight_search_view, name='flight_search'),
    path('flights/', FlightListView.as_view(), name='flight_list'),

    # Passenger listing
    path('passengers/', PassengerListView.as_view(), name='passenger_list'),
]
