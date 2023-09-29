from django.shortcuts import render
from .models import *
import sqlite3


def Home(request):
    return render(request, 'ToDo_app/home.html')


