from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookings.models import Booking
from .serializers import BookingSerializer
from flights.models import Flight

from .serializers import FlightSerializer

@api_view(['GET'])
def booking_api(request):

    bookings = Booking.objects.all()

    serializer = BookingSerializer(
        bookings,
        many=True
    )

    return Response(
        serializer.data
    )

@api_view(['GET'])
def flight_api(request):

    flights = Flight.objects.all()

    serializer = FlightSerializer(
        flights,
        many=True
    )

    return Response(
        serializer.data
    )

@api_view(['GET'])
def api_root(request):

    return Response({
        'flights': '/api/flights/',
    })
