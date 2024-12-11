"""
Views for the final_project app.

Includes:
- Generic class-based views for Airline (CRUD).
- A function-based view for searching/filtering Flights.
- Additional list views for Flight and Passenger.
Each view includes docstrings explaining its purpose.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib import messages

from .models import Airline, Airport, Flight, Passenger
from .forms import AirlineForm, FlightSearchForm


# --------------------------------------------
# Airline Views (CRUD using Class-Based Views)
# --------------------------------------------

class AirlineListView(ListView):
    """
    Displays a list of all Airline objects.
    """
    model = Airline
    template_name = 'final_project/airline_list.html'
    context_object_name = 'airlines'


class AirlineDetailView(DetailView):
    """
    Displays the details of a single Airline object.
    """
    model = Airline
    template_name = 'final_project/airline_detail.html'
    context_object_name = 'airline'


class AirlineCreateView(CreateView):
    """
    Displays a form to create a new Airline object and saves it to the database.
    Uses AirlineForm for validation and rendering.
    """
    model = Airline
    form_class = AirlineForm
    template_name = 'final_project/airline_form.html'
    success_url = reverse_lazy('final_project:airline_list')

    def form_valid(self, form):
        messages.success(self.request, "Airline created successfully!")
        return super().form_valid(form)


class AirlineUpdateView(UpdateView):
    """
    Displays a form to update an existing Airline object.
    """
    model = Airline
    form_class = AirlineForm
    template_name = 'final_project/airline_form.html'
    success_url = reverse_lazy('final_project:airline_list')

    def form_valid(self, form):
        messages.success(self.request, "Airline updated successfully!")
        return super().form_valid(form)


class AirlineDeleteView(DeleteView):
    """
    Displays a confirmation page to delete an existing Airline object.
    """
    model = Airline
    template_name = 'final_project/airline_confirm_delete.html'
    success_url = reverse_lazy('final_project:airline_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Airline deleted successfully!")
        return super().delete(request, *args, **kwargs)


# --------------------------------------------
# Flight Views
# --------------------------------------------

def flight_search_view(request):
    """
    A function-based view that allows users to search for flights by airline code 
    or origin airport code. Returns a filtered list of flights based on the criteria.
    """
    form = FlightSearchForm(request.GET or None)
    flights = Flight.objects.all()

    if form.is_valid():
        airline_code = form.cleaned_data.get('airline_code')
        origin_code = form.cleaned_data.get('origin_code')

        if airline_code:
            flights = flights.filter(airline__code__icontains=airline_code)
        if origin_code:
            flights = flights.filter(origin__code__icontains=origin_code)

    context = {
        'form': form,
        'flights': flights
    }
    return render(request, 'final_project/flight_search.html', context)


class FlightListView(ListView):
    """
    Displays a list of all Flight objects.
    """
    model = Flight
    template_name = 'final_project/flight_list.html'
    context_object_name = 'flights'


# --------------------------------------------
# Passenger Views
# --------------------------------------------

class PassengerListView(ListView):
    """
    Displays a list of all Passenger objects. This is a simple read-only view for demonstration.
    """
    model = Passenger
    template_name = 'final_project/passenger_list.html'
    context_object_name = 'passengers'
