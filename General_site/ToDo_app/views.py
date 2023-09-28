from django.shortcuts import render
from .models import *


def Home(request):
    return render(request, 'ToDo_app/home.html')


def Add(request):
    object_list = Model_Memory.objects.all()
    return render(request, 'ToDo_app/add.html', {'objects_list': object_list})


def Added(request):
    topic = request.POST['topic']
    date = request.POST['date']
    elems = Model_Memory(topic=topic, time=date)
    elems.save()
    return render(request, 'ToDo_app/added_page.html', {'topic': topic,
                                                        'date': date})

def All(request):
    bd = list(Model_Memory.objects.all())
    return render(request, 'ToDo_app/mynote.html', {'position' : bd})