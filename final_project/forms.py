"""
Forms for the final_project app. Includes model forms for CRUD operations and 
a search form for filtering flights.
"""
from django import forms
from .models import Airline, Flight

class AirlineForm(forms.ModelForm):
    """
    A form for creating and updating Airline instances.
    """
    class Meta:
        model = Airline
        fields = ['name', 'code']


class FlightSearchForm(forms.Form):
    """
    A form for searching flights by airline code or origin airport code.
    """
    airline_code = forms.CharField(
        max_length=10, 
        required=False, 
        help_text="Enter the airline code to filter flights."
    )
    origin_code = forms.CharField(
        max_length=10, 
        required=False, 
        help_text="Enter the origin airport code to filter flights."
    )
