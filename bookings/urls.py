from django.urls import path
from .views import create_booking, cancel_booking, my_bookings
from .views import flight_list

urlpatterns = [
    path("book/<int:flight_id>/", create_booking, name="create_booking"),
    path("cancel/<int:booking_id>/", cancel_booking, name="cancel_booking"),
    path("my/", my_bookings, name="my_bookings"),
    path("", flight_list, name="flight_list"),
]
