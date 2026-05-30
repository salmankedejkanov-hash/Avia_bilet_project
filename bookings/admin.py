from django.contrib import admin
from .models import Booking, Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "date", "price")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "flight", "user", "is_paid", "created_at")
    list_filter = ("is_paid", "created_at")
