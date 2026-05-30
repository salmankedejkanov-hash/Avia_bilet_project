from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "flight", "is_paid", "created_at")
    list_filter = ("is_paid", "created_at")
    search_fields = ("user__username", "flight__origin", "flight__destination")
