from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f" title: {self.title}, content: {self.content[:30]} author: {self.author_id}"

class Author(models.Model):
    nick = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"nick: {self.nick}, email: {self.email}"