from django.urls import path
from .views import MainTaxiView, YandexTaxiView, NambaTaxiView, JorgoTaxiView


urlpatterns = [
    path("taxi/", MainTaxiView.as_view(), name="taxi_main"),
    path("taxi/yandex/", YandexTaxiView.as_view(), name="taxi_yandex"),
    path("taxi/namba/", NambaTaxiView.as_view(), name="taxi_namba"),
    path("taxi/jorgo/", JorgoTaxiView.as_view(), name="taxi_jorgo"),

]