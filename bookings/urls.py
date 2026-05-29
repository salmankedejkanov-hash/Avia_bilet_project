from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.booking_list,
        name='booking_list'
    ),

    path(
        'my/',
        views.my_bookings,
        name='my_bookings'
    ),

    path(
        'create/',
        views.create_booking,
        name='create_booking'
    ),
]
