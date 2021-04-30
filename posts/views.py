from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Post, Author
from .forms import PostForm, AuthorForm

# Create your views here.
def posts_list(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy post!")
        return HttpResponseRedirect("")
    posts = Post.objects.all().order_by("created")
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"posts": posts, "form": form}
    )

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post}
    )

def authors_list(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowego autora!")
        return HttpResponseRedirect("")

    authors = Author.objects.all().order_by("nick")
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"authors": authors, "form": form}
    )

def author_details(request, id):
    author = get_object_or_404(Author, id=id)
    posts = Post.objects.filter(author=author)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author, "posts": posts}
    )
