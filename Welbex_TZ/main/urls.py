from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index_urls'),
    path('filter_car', FilterCar.as_view(), name='filter_car_urls')
]