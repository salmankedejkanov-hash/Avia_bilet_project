from rest_framework import viewsets
from flights.models import Flight
from bookings.models import Booking
from .serializers import FlightSerializer, BookingSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
