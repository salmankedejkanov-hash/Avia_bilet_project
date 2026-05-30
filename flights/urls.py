from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:pk>/', views.flight_detail, name='flight_detail'),
    path('<int:pk>/book/', views.book_flight, name='book_flight'),
]
