from django.shortcuts import render
from .models import Booking
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

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

            form.add_error(
                None,
                "No available seats."
            )

        else:

            booking.save()

            flight = booking.flight

            flight.seats -= 1

            flight.save()

            return redirect(
                'booking_list'
            )

    context = {
        'form': form
    }

    return render(
        request,
        'bookings/create_booking.html',
        context
    )
