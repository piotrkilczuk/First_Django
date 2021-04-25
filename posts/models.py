from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
        blank=False
    )

    def __str__(self):
        return f" T: {self.title}, C: {self.content[:30]} A: {self.author.nick}"

class Author(models.Model):
    nick = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"N: {self.nick}, E: {self.email}"