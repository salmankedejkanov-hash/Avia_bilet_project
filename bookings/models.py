from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origin} → {self.destination}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.flight}"
