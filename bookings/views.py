from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/my_bookings.html', {
        'bookings': bookings
    })


@login_required
def cancel_booking(request, pk):

    booking = Booking.objects.get(id=pk, user=request.user)
    booking.status = 'cancelled'
    booking.save()

    return redirect('my_bookings')
