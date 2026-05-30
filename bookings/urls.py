from django.urls import path
from .views import my_bookings, cancel_booking

urlpatterns = [
    path('my/', my_bookings, name='my_bookings'),
    path('cancel/<int:pk>/', cancel_booking, name='cancel_booking'),
]
