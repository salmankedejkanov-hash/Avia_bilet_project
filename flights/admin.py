from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'airline',
        'departure_airport',
        'arrival_airport',
        'price',
        'seats',
        'status',
    )

    list_filter = (
        'airline',
        'status',
    )

    search_fields = (
        'departure_airport__city',
        'arrival_airport__city',
    )

    ordering = (
        '-departure_time',
    )