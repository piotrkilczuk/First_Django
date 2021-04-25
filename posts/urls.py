from django.urls import path
from .views import posts_list, post_details, authors_list, author_details

app_name = "posts"
urlpatterns = [
    path('', posts_list, name="posts_list"),
    path('<int:id>/', post_details, name="post_details"),
    path('authors/', authors_list, name="authors_list"),
    path('authors/<int:id>/', author_details, name="author_details"),
]