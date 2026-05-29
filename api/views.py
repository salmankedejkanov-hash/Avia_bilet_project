from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookings.models import Booking
from .serializers import BookingSerializer
from flights.models import Flight

from .serializers import FlightSerializer

@api_view(['POST'])
def booking_create_api(request):

    serializer = BookingSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=201
        )

    return Response(
        serializer.errors,
        status=400
    )

@api_view(['GET'])
def flight_detail_api(request, pk):

    flight = Flight.objects.get(id=pk)

    serializer = FlightSerializer(
        flight
    )

    return Response(
        serializer.data
    )

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
