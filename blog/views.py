from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts': posts})
