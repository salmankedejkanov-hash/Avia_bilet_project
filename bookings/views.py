from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Booking
from .forms import BookingForm


@login_required
def booking_list(request):

    bookings = Booking.objects.all()

    context = {
        'bookings': bookings
    }

    return render(
        request,
        'bookings/booking_list.html',
        context
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    )

    context = {
        'bookings': bookings
    }

    return render(
        request,
        'bookings/my_bookings.html',
        context
    )


@login_required
def create_booking(request):

    form = BookingForm(
        request.POST or None
    )

    if form.is_valid():

        booking = form.save(
            commit=False
        )

        booking.user = request.user

        if booking.flight.seats <= 0:

            messages.error(
                request,
                'No available seats.'
            )

        else:

            booking.save()

            flight = booking.flight

            flight.seats -= 1

            flight.save()

            messages.success(
                request,
                'Ticket booked successfully.'
            )

            return redirect(
                'my_bookings'
            )

    context = {
        'form': form
    }

    return render(
        request,
        'bookings/create_booking.html',
        context
    )