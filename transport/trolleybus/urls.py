from django.urls import path
from .views import MainTrolleybusView, Trolleybus_5_View, Trolleybus_7_View, Trolleybus_17_View, Trolleybus_10_View


urlpatterns = [
    path("trolleybus/", MainTrolleybusView.as_view(), name="trolleybus_main"),
    path("trolleybus/5/", Trolleybus_5_View.as_view(), name="trolleybus_5"),
    path("trolleybus/7/", Trolleybus_7_View.as_view(), name="trolleybus_7"),
    path("trolleybus/17/", Trolleybus_17_View.as_view(), name="trolleybus_17"),
    path("trolleybus/10/", Trolleybus_10_View.as_view(), name="trolleybus_10"),
]