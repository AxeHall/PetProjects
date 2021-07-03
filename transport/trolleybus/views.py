from django.shortcuts import render
from django.views.generic import View

class MainTrolleybusView(View):
    def get(self, request):
        return render(request, template_name="trolleybus/index.html")

class Trolleybus_5_View(View):
    def get(self, request):
        return render(request, template_name="trolleybus/trolleybus5.html")

class Trolleybus_7_View(View):
    def get(self, request):
        return render(request, template_name="trolleybus/trolleybus7.html")

class Trolleybus_17_View(View):
    def get(self, request):
        return render(request, template_name="trolleybus/trolleybus17.html")

class Trolleybus_10_View(View):
    def get(self, request):
        return render(request, template_name="trolleybus/trolleybus10.html")

# Create your views here.
