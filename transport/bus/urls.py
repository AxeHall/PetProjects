from django.urls import path
from .views import MainBusView, Bus102View, Bus169View, Bus172View, Bus212View

urlpatterns = [
    path("bus/", MainBusView.as_view(), name="bus_main"),
    path("bus/102/", Bus102View.as_view(), name="bus_102"),
    path("bus/169/", Bus169View.as_view(), name="bus_169"),
    path("bus/172/", Bus172View.as_view(), name="bus_172"),
    path("bus/212/", Bus212View.as_view(), name="bus_212"),
]