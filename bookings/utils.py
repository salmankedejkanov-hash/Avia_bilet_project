from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Booking

def generate_ticket_pdf(booking_id):
    booking = Booking.objects.get(id=booking_id)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, 800, "✈ AIR TICKET")

    p.setFont("Helvetica", 12)
    p.drawString(100, 770, f"Passenger: {booking.user}")
    p.drawString(100, 750, f"Route: {booking.flight.origin} → {booking.flight.destination}")
    p.drawString(100, 730, f"Booking ID: {booking.id}")

    status = "PAID ✔" if booking.is_paid else "NOT PAID ❌"
    p.drawString(100, 710, f"Status: {status}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

import qrcode
from io import BytesIO

def generate_qr(booking):
    data = f"BOOKING:{booking.id}|{booking.flight.id}|{booking.user.id}"

    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer)
    buffer.seek(0)

    return buffer
