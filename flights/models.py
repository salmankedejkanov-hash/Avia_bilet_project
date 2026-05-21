
from django.db import models
from airlines.models import Airline
from airports.models import Airport


class Flight(models.Model):

    airline = models.ForeignKey(
        Airline,
        on_delete=models.CASCADE
    )

    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('boarding', 'Boarding'),
        ('departed', 'Departed'),
        ('cancelled', 'Cancelled'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )

    departure_airport = models.ForeignKey(
        Airport,
        related_name='departures',
        on_delete=models.CASCADE
    )

    arrival_airport = models.ForeignKey(
        Airport,
        related_name='arrivals',
        on_delete=models.CASCADE
    )

    departure_time = models.DateTimeField()

    arrival_time = models.DateTimeField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    seats = models.IntegerField()

    def __str__(self):
        return f"{self.departure_airport} → {self.arrival_airport}"