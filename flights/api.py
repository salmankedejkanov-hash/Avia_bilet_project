from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight

@api_view(['GET'])
def flights_api(request):
    flights = Flight.objects.all()

    data = [
        {
            "id": f.id,
            "origin": f.origin,
            "destination": f.destination,
            "price": f.price
        }
        for f in flights
    ]

    return Response(data)

@api_view(['GET'])
def flights_api(request):
    flights = Flight.objects.all()

    data = [
        {
            "id": f.id,
            "origin": f.origin,
            "destination": f.destination,
            "price": f.price
        }
        for f in flights
    ]

    return Response(data)

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
