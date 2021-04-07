from django.shortcuts import render
from django.http import HttpResponse

def greet(request, name=""):
    if name:
        return HttpResponse(f"Hello {name.capitalize()}!")

    return HttpResponse("Hello World!")
