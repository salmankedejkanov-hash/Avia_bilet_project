from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flight, Booking


def flight_list(request):
    flights = Flight.objects.all()
    return render(request, "flights/flight_list.html", {"flights": flights})


@login_required
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    Booking.objects.create(
        user=request.user,
        flight=flight,
        full_name=request.user.username
    )

    return redirect("my_bookings")


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect("my_bookings")