
# Register your models here.
from django.contrib import admin
from .models import Airline, Passenger

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

admin.site.register(Passenger)