from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_ticket_email(booking):
    subject = "✈ Ваш авиабилет"
    from_email = "no-reply@avia.com"
    to = [booking.user.email]

    html = render_to_string("bookings/email_ticket.html", {
        "booking": booking
    })

    msg = EmailMultiAlternatives(subject, "", from_email, to)
    msg.attach_alternative(html, "text/html")
    msg.send()
