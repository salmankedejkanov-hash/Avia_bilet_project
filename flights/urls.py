from django.urls import path
from .views import flight_list, flight_search_api

urlpatterns = [
    path('', flight_list, name='flight_list'),
    path('api/search/', flight_search_api, name='flight_search_api'),
]