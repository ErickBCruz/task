from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tarea(request):
    return HttpResponse('tarea')