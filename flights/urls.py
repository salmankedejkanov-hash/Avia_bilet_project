from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.flight_list,
        name='flight_list'
    ),

    path(
        '<int:pk>/',
        views.flight_detail,
        name='flight_detail'
    ),

    path(
        'create/',
        views.create_flight,
        name='create_flight'
    ),

    path(
        '<int:pk>/update/',
        views.update_flight,
        name='update_flight'
    ),

    path(
        '<int:pk>/delete/',
        views.delete_flight,
        name='delete_flight'
    ),
]
