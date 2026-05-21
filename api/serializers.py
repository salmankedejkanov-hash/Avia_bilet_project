from rest_framework import serializers

from flights.models import Flight
from bookings.models import Booking


class FlightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Flight

        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking

        fields = [
            'id',
            'user',
            'flight',
            'seat_number',
            'status',
            'booking_date'
        ]