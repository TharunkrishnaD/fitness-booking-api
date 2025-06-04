from django.urls import path
from . import views


urlpatterns = [
    path('booking/', 
        views.BookingAPIView.as_view(), 
        name='booking_class'
    ),
    path('booking-list/', 
        views.BookingListAPIView.as_view(), 
        name='booking_list'
    ),
]