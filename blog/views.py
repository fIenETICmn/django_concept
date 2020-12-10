from django.shortcuts import render, redirect
from .models import User, Post
from django.utils import timezone
from django.contrib.auth import login, authenticate
from .forms import SignupForm, PostForm


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})