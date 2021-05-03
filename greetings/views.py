from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def homepage(request):
      return render(
            request=request,
            template_name="greetings/homepage.html",
            context={"title": "Homepage"}
      )

def about_me(request):
      return render(
            request=request,
            template_name="greetings/me.html",
            context={"title": "About me"}
      )

def contact(request):
      return render(
            request=request,
            template_name="greetings/contact.html",
            context={"title": "Contact"}
      )