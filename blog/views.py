from django.shortcuts import render, redirect
from .models import Post, Product, Store
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, ProductForm, PostForm, StoreForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    return render(request, 'index.html')


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def product_list(request):
    products = Product.objects.filter()
    return render(request, 'product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def store_list(request):
    storelist = Store.objects.all()
    return render(request, 'store_list.html', {'storelist': storelist})


def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            # store.author = request.user
            store.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    return render(request, 'add_store.html', {'form': form})


def store_product_list(request):
    # storel = Store.objects.get(id=id)
    # store_product = Product.objects.filter(store=storel)
    store_product = Store.objects.filter(product__id=id)
    return render(request, 'store_list.html', {'store_product': store_product})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')