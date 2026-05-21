from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'flight',
        'seat_number',
        'status',
        'booking_date',
    )

    search_fields = (
        'user__username',
        'seat_number',
    )

    list_filter = (
        'status',
        'booking_date',
    )