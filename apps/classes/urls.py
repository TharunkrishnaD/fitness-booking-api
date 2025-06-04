from django.urls import path
from . import views


urlpatterns = [
    path('class-list/', 
    views.ClassListAPIView.as_view(), 
    name='class_list'),
]