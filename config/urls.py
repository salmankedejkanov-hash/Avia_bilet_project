from django.contrib import admin
from django.urls import path, include

from config.views import home

from rest_framework.routers import DefaultRouter
from flights.api import FlightViewSet
from bookings.api import BookingViewSet


# API ROUTER
router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('bookings', BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME PAGE
    path('', home, name='home'),

    # APPS
    path('flights/', include('flights.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),

    # API
    path('api/', include(router.urls)),
]
