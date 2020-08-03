from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def Hposts(request):
    posts = Post.objects.filter(type = 'Hobby')
    return render(request, 'blog/posts.html', {'posts': posts})


def Pposts(request):
    posts = Post.objects.filter(type = 'Project')
    return render(request, 'blog/postsProj.html', {'posts': posts})


def main(request):
    return render(request, 'main.html')


def post(request, name):
    post = Post.objects.filter(title=name)[0]
    return render(request, 'blog/post_temp.html', {'post' : post})
