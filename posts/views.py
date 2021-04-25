from django.shortcuts import render
from django.contrib import messages

from .models import Post, Author
from .forms import PostForm, AuthorForm

# Create your views here.
def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            # Mam wrażenie, że można uprościć ilość kodu. Podejrzewam, że w formularzu, może za pomocą clean()? 
            # Przy request.POST wywala błąd o MultiDict
            Post.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                author=Author.objects.get(id=request.POST['author'])
                )

            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy post!")
    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"posts": posts, "form": form}
    )

def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post}
    )

def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            Author.objects.get_or_create(
                nick=request.POST['nick'],
                email=request.POST['email']
                )[0]
                
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!")
    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"authors": authors, "form": form}
    )

def author_details(request, id):
    author = Author.objects.get(id=id)
    posts = Post.objects.filter(author=author).all()
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author, "posts": posts}
    )
