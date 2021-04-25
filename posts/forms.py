from django.forms import ModelForm
from .models import Post, Author

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'email']