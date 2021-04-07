from django.shortcuts import render
from django.http import HttpResponse

def greet(request):
    return HttpResponse("Hello World!")

def name_greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")