from django.urls import path
from . import views
from .views import home   # ✅ ВОТ ЭТО ОБЯЗАТЕЛЬНО
from .views import flight_list
from .views import flight_list, flight_search_api


urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:pk>/', views.flight_detail, name='flight_detail'),
    path('<int:pk>/book/', views.book_flight, name='book_flight'),
    path('', home, name='home'),
    path('', flight_list, name='flight_list'),
    path('', flight_list, name='flight_list'),
    path('api/search/', flight_search_api, name='flight_search_api'),
    path("api/flights/", flights_api),
]
