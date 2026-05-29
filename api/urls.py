from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.api_root,
        name='api_root'
    ),
    path(
        'bookings/',
        views.booking_api,
        name='booking_api'
    ),
    path(
        'flights/<int:pk>/',
        views.flight_detail_api,
        name='flight_detail_api'
    ),
    path(
        'bookings/create/',
        views.booking_create_api,
        name='booking_create_api'
    ),
    path(
        'flights/',
        views.flight_api,
        name='flight_api'
    ),
]