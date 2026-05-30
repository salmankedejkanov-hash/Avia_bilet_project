from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Booking
from flights.models import Flight
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking
from django.shortcuts import render
from .models import Flight

def flight_list(request):
    flights = Flight.objects.all()

    return render(request, "flights/flights_list.html", {
        "flights": flights
    })


# ✈ создать бронь
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    # защита от дубля
    if Booking.objects.filter(user=request.user, flight=flight).exists():
        return JsonResponse({"success": False, "message": "Уже забронировано"})

    booking = Booking.objects.create(
        user=request.user,
        flight=flight
    )

    return JsonResponse({
        "success": True,
        "booking_id": booking.id
    })


# ❌ отмена брони
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()

    return JsonResponse({"success": True})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, "bookings/my_bookings.html", {
        "bookings": bookings
    })
