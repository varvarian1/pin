from django.shortcuts import render
from pin_create_tool.models import *

def index(request):
    pins = Pin.objects.all()
    return render(request, 'main/main.html', {'pins': pins})

