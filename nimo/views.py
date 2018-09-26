from django.shortcuts import render, redirect
import datetime as dt
from .forms import PostForm
from .models import Blog

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def post(request):
    form= PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('welcome')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form":form})
