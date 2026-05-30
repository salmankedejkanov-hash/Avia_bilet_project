from django.urls import path
from . import views

urlpatterns = [
    path("", views.flight_list, name="flights"),
    path("book/<int:flight_id>/", views.create_booking, name="create_booking"),
    path("my/", views.my_bookings, name="my_bookings"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
