from django.urls import path
from .views import math, add, sub, mul, div

urlpatterns = [
    path('', math),
    path('add/<a>/<b>', add),
    path('sub/<a>/<b>', sub),
    path('mul/<a>/<b>', mul),
    path('div/<a>/<b>', div),
]