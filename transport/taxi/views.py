from django.shortcuts import render
from django.views.generic import View

class MainTaxiView(View):
    def get(self, request):
        return render(request, template_name="taxi/index.html")

class YandexTaxiView(View):
    def get(self, request):
        return render(request, template_name="taxi/yandex_taxi.html")

class NambaTaxiView(View):
    def get(self, request):
        return render(request, template_name="taxi/namba_taxi.html")

class JorgoTaxiView(View):
    def get(self, request):
        return render(request, template_name="taxi/jorgo_taxi.html")

# Create your views here.
