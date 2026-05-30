from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from bookings.models import Booking
from django.shortcuts import render
from .models import Flight

def flight_list(request):

    flights = Flight.objects.all()

    # поиск по городу
    search = request.GET.get('search')

    # фильтр "откуда"
    departure = request.GET.get('departure')

    # фильтр "куда"
    arrival = request.GET.get('arrival')

    # сортировка
    sort = request.GET.get('sort')

    if search:
        flights = flights.filter(
            arrival_airport__city__icontains=search
        )

    if departure:
        flights = flights.filter(
            departure_airport__city__icontains=departure
        )

    if arrival:
        flights = flights.filter(
            arrival_airport__city__icontains=arrival
        )

    if sort == 'cheap':
        flights = flights.order_by('price')

    if sort == 'expensive':
        flights = flights.order_by('-price')

    return render(request, 'flights/flight_list.html', {
        'flights': flights
    })


def flight_detail(request, pk):

    flight = get_object_or_404(Flight, id=pk)

    return render(request, 'flights/flight_detail.html', {
        'flight': flight
    })


@login_required
def book_flight(request, pk):

    flight = Flight.objects.get(id=pk)

    booking, created = Booking.objects.get_or_create(
        user=request.user,
        flight=flight
    )

    if not created:
        # если уже забронировано — просто не создаём дубль
        pass

    return redirect('my_bookings')

