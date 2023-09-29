from django.shortcuts import render
from .models import *


def Home(request):
    return render(request, 'ToDo_app/home.html')


