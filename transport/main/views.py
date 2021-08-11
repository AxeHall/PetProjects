from django.shortcuts import render
from django.views.generic import View


class MainView(View):
    def get(self, request):
        return render(request, template_name="main/index.html")

# Create your views here.
