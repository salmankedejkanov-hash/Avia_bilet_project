from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Flight
from .forms import FlightForm


def home(request):

    return render(
        request,
        'home.html'
    )


def flight_list(request):

    flights = Flight.objects.all()

    search = request.GET.get('search')

    if search:

        flights = flights.filter(

            Q(
                departure_airport__city__icontains=search
            ) |

            Q(
                arrival_airport__city__icontains=search
            )
        )

    paginator = Paginator(
        flights,
        5
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

    flight = Flight.objects.get(id=pk)

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
        'flights/update_flight.html',
        context
    )


def delete_flight(request, pk):

    flight = Flight.objects.get(id=pk)

    if request.method == 'POST':

        flight.delete()

        return redirect(
            'flight_list'
        )

    context = {
        'flight': flight
    }

    return render(
        request,
        'flights/delete_flight.html',
        context
    )

def flight_detail(request, pk):

    flight = Flight.objects.get(id=pk)

    context = {
        'flight': flight
    }

    return render(
        request,
        'flights/flight_detail.html',
        context
    )
