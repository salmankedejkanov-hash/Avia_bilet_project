from . import views
from django.urls import path
from .views import my_bookings

urlpatterns = [
    path('my/', my_bookings, name='my_bookings'),
]

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:pk>/', views.flight_detail, name='flight_detail'),
    path('<int:pk>/book/', views.book_flight, name='book_flight'),
]
