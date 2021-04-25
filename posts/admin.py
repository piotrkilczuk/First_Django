from django.contrib import admin
from posts.models import Post, Author
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created", "modified", "author"]
    list_filter = ["title", "author__nick"]
    search_fields = ["title", "author__nick"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "nick", "email"]
    list_filter = ["nick", "email"]
    search_fields = ["nick", "email"]
