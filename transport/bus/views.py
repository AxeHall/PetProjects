from django.shortcuts import render
from django.views.generic import View

class MainBusView(View):
    def get(self, request):
        return render(request, template_name="bus/index.html")

class Bus102View(View):
    def get(self, request):
        return render(request, template_name="bus/bus102.html")

class Bus169View(View):
    def get(self, request):
        return render(request, template_name="bus/bus169.html")

class Bus172View(View):
    def get(self, request):
        return render(request, template_name="bus/bus172.html")

class Bus212View(View):
    def get(self, request):
        return render(request, template_name="bus/bus212.html")


# Create your views here.
