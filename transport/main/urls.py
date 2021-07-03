from django import urls
from django.urls import path
from .views import MainView


urlpatterns = [
    path("main/", MainView.as_view(), name="main")
]