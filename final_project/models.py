from django.db import models

class Airline(models.Model):
    """
    Represents an airline, which can exist independently without foreign keys.
    Includes basic identification information about the airline.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the airline,
        combining the airline's name and its code.
        """
        return f"{self.name} ({self.code})"


class Airport(models.Model):
    """
    Represents an airport, which also can exist independently.
    Each airport is identified by a unique code and associated city and country.
    """
    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation that displays the airport's city and code.
        This makes it easy to identify the airport in admin interfaces or logs.
        """
        return f"{self.city} - {self.code}"


class Flight(models.Model):
    """
    Represents a flight that connects an origin airport to a destination airport
    and is operated by an airline. Each flight has scheduled departure and arrival times.
    """
    airline = models.ForeignKey(
        Airline,
        on_delete=models.CASCADE,
        related_name='flights',
        help_text="The airline operating this flight."
    )
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='departing_flights',
        help_text="The originating airport of the flight."
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='arriving_flights',
        help_text="The destination airport of the flight."
    )
    departure_time = models.DateTimeField(help_text="When the flight is scheduled to depart.")
    arrival_time = models.DateTimeField(help_text="When the flight is scheduled to arrive.")

    def __str__(self):
        """
        Returns a string representation of the flight, displaying the airline code
        and the route from the origin airport's code to the destination airport's code.
        This makes it easier to distinguish between multiple flights at a glance.
        """
        return f"{self.airline.code} Flight from {self.origin.code} to {self.destination.code}"


class Passenger(models.Model):
    """
    Represents a passenger booked on a particular flight.
    Passengers are associated with flights via a foreign key, meaning each passenger record
    is linked to a specific flight.
    """
    first_name = models.CharField(max_length=50, help_text="The passenger's first name.")
    last_name = models.CharField(max_length=50, help_text="The passenger's last name.")
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name='passengers',
        help_text="The flight this passenger is booked on."
    )

    def __str__(self):
        """
        Returns a string representation of the passenger, including their full name
        and the flight they are associated with. This helps identify which passenger
        is on which flight in admin interfaces and logs.
        """
        return f"{self.first_name} {self.last_name} on {self.flight}"
