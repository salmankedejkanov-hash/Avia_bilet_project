from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from flights.models import Flight


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    seat_number = models.CharField(
        max_length=10
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        unique_together = (
            'flight',
            'seat_number'
        )

        ordering = ['-booking_date']

    def __str__(self):

        return (
            f"{self.user.username} | "
            f"{self.flight} | "
            f"Seat {self.seat_number}"
        )

    def clean(self):
        if self.flight.seats <= 0:
            raise ValidationError(
                'No available seats.'
            )