from django.urls import path
from .views import greet, name_greet

urlpatterns = [
    path('', greet),
    path('<str:name>', name_greet),
]