from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'flights/',
        views.flight_list,
        name='flight_list'
    ),

    path(
        'flights/create/',
        views.create_flight,
        name='create_flight'
    ),

    path(
        'flights/<int:pk>/update/',
        views.update_flight,
        name='update_flight'
    ),

    path(
        'flights/<int:pk>/delete/',
        views.delete_flight,
        name='delete_flight'
    ),

    path(
        'flights/<int:pk>/',
        views.flight_detail,
        name='flight_detail'
    ),
]