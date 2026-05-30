from flights.models import Flight
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Booking
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import send_mail

send_mail(
    "Бронь подтверждена",
    f"Ваш билет: {flight.origin} → {flight.destination}",
    "your_email@gmail.com",
    [request.user.email],
    fail_silently=True
)

@login_required
def download_ticket(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{booking.id}.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 800, "AIR TICKET")
    p.drawString(100, 770, f"Passenger: {request.user.username}")
    p.drawString(100, 750, f"From: {booking.flight.origin}")
    p.drawString(100, 730, f"To: {booking.flight.destination}")
    p.drawString(100, 710, f"Price: {booking.flight.price}")
    p.drawString(100, 690, f"Booking ID: {booking.id}")

    p.showPage()
    p.save()

    return response


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect("my_bookings")


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('flight')

    return render(request, "bookings/my_bookings.html", {
        "bookings": bookings
    })

@login_required
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    Booking.objects.create(
        user=request.user,
        flight=flight
    )

    return redirect("my_bookings")

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

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, "bookings/my_bookings.html", {
        "bookings": bookings
    })
