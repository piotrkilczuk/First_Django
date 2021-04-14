from django.shortcuts import render
from django.http import HttpResponse

def greet(request, name="World"):
    return HttpResponse(f"Hello {name.capitalize()}!")