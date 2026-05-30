from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from bookings.models import Booking

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from flights.models import Flight
from .models import Flight


@login_required
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    Booking.objects.create(
        user=request.user,
        flight=flight
    )

    return JsonResponse({
        "success": True,
        "message": "Бронь создана"
    })


def flight_search_api(request):
    origin = request.GET.get("origin", "")
    destination = request.GET.get("destination", "")
    max_price = request.GET.get("max_price", "")

    flights = Flight.objects.all()

    if origin:
        flights = flights.filter(origin__icontains=origin)

    if destination:
        flights = flights.filter(destination__icontains=destination)

    if max_price:
        flights = flights.filter(price__lte=max_price)

    data = list(flights.values("id", "origin", "destination", "price"))

    return JsonResponse({"flights": data})

def flight_list(request):
    flights = Flight.objects.all()

    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    max_price = request.GET.get('max_price')

    if origin:
        flights = flights.filter(origin__icontains=origin)

    if destination:
        flights = flights.filter(destination__icontains=destination)

    if max_price:
        flights = flights.filter(price__lte=max_price)

    return render(request, "flights/flight_list.html", {
        "flights": flights
    })

def home(request):
    flights = Flight.objects.all()

    origin = request.GET.get('origin')
    destination = request.GET.get('destination')

    if origin:
        flights = flights.filter(origin__city__icontains=origin)

    if destination:
        flights = flights.filter(destination__city__icontains=destination)

    context = {
        'flights': flights
    }
    return render(request, 'flights/home.html', context)


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

