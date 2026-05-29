
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from bookings.models import Booking
from .models import Flight

@login_required
def book_flight(request, pk):

    flight = Flight.objects.get(id=pk)

    Booking.objects.get_or_create(
        user=request.user,
        flight=flight
    )

    return redirect('my_bookings')

def flight_list(request):

    flights = Flight.objects.all()

    search = request.GET.get('search')

    if search:
        flights = flights.filter(
            arrival_airport__city__icontains=search
        )

    return render(request, 'flights/flight_list.html', {
        'flights': flights
    })

@login_required
def book_flight(request, pk):

    flight = Flight.objects.get(id=pk)

    Booking.objects.create(
        user=request.user,
        flight=flight
    )

    return redirect('my_bookings')
