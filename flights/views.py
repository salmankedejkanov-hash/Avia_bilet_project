from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from .models import Flight

from .forms import FlightForm
from django.shortcuts import render
from .models import Flight


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

def flight_list(request):

    flights = Flight.objects.all()

    search = request.GET.get('search')

    if search:

        flights = flights.filter(
            arrival_airport__city__icontains=search
        )

    paginator = Paginator(
        flights,
        6
    )

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(
        page_number
    )

    context = {
        'page_obj': page_obj
    }

    return render(
        request,
        'flights/flight_list.html',
        context
    )


def flight_detail(request, pk):

    flight = get_object_or_404(
        Flight,
        id=pk
    )

    context = {
        'flight': flight
    }

    return render(
        request,
        'flights/flight_detail.html',
        context
    )


def create_flight(request):

    form = FlightForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'flight_list'
        )

    context = {
        'form': form
    }

    return render(
        request,
        'flights/create_flight.html',
        context
    )


def update_flight(request, pk):

    flight = get_object_or_404(
        Flight,
        id=pk
    )

    form = FlightForm(
        request.POST or None,
        instance=flight
    )

    if form.is_valid():

        form.save()

        return redirect(
            'flight_list'
        )

    context = {
        'form': form
    }

    return render(
        request,
        'flights/create_flight.html',
        context
    )


def delete_flight(request, pk):

    flight = get_object_or_404(
        Flight,
        id=pk
    )

    flight.delete()

    return redirect(
        'flight_list'
    )
