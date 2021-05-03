from django.urls import path
from .views import homepage, about_me, contact

app_name = "greetings"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('me/', about_me, name="about_me"),
    path('contact/', contact, name="contact"),
]