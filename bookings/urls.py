from django.urls import path
from .views import create_booking, my_bookings

urlpatterns = [
    path("book/<int:flight_id>/", create_booking, name="create_booking"),
    path("my/", my_bookings, name="my_bookings"),
    path("book/<int:flight_id>/", create_booking, name="create_booking"),
    path("my/", my_bookings, name="my_bookings"),
    path("cancel/<int:booking_id>/", cancel_booking, name="cancel_booking"),
    path("ticket/<int:booking_id>/", download_ticket, name="ticket"),
]