from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# Create a view with the 3 latest posts and render a template with the posts
def index(request):
    latest_posts = Post.objects.all()[:3]
    context = {"posts":latest_posts}
    return render(request, "blog/index.html",context)

# Create a view with all posts and render a template with the posts
def posts(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, "blog/posts.html", context)