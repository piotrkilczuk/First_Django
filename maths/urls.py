from django.urls import path
from .views import math, add, sub, mul, div, maths_list, math_details, results_list

app_name = "maths"
urlpatterns = [
    path('', math),
    path('add/<a>/<b>', add),
    path('sub/<a>/<b>', sub),
    path('mul/<a>/<b>', mul),
    path('div/<a>/<b>', div),
    path('histories/', maths_list, name="list"),
    path('histories/<int:id>', math_details, name="details"),
    path('results/', results_list, name="results"),
]