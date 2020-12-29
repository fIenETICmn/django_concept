from .models import Post, Product, Store, Cart, Order, Category
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, ProductForm, PostForm, StoreForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# from django.db.models import Q


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


def category_list(request):
    categorylist = Category.objects.all()
    return render(request, 'category_list.html', {'categorylist': categorylist})


def category_product_list(request, pk):
    # categoryl = Category.objects.get(id=pk)
    # category_product = Product.objects.filter(category=categoryl)
    category_product = Product.objects.filter(category__id=pk)
    return render(request, 'category_product_list.html', {'category_product': category_product})


def filter_product(request):
    # print(request.GET["filter_type"])
    if 'filter_type' in request.GET and request.GET["filter_type"] == "low":
        fill_products = Product.objects.filter().order_by('price')
    else:
        fill_products = Product.objects.filter().order_by('-price')
    # print(Products.query)
    return render(request, 'product_list.html', {'fill_products': fill_products})


def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = Cart.objects.get_or_create(item=item, user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"{item.name} quantity has update.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            order.orderitems.add(order_item)
            messages.info(request, f"{item.name} has added to your cart.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        order = Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, f"{item.name} has added to your cart. ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_view(request):
    user = request.user
    carts = Cart.objects.filter(user=user, price=False)
    orders = Order.objects.filter(user=user, ordered=False)
    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'cart.html', {'carts': carts, 'order': order})
        else:
            messages.warning(request, "You do not have any item in your wishlist")
            return redirect('product_list')
    else:
        messages.warning(request, "You do not have any item in your wishlist")
        return redirect('product_list')

    return render(request, 'cart.html', {'carts': carts})


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


def store_product_list(request, pk):
    # storel = Store.objects.get(id=pk)
    # store_product = Product.objects.filter(store=storel)
    store_product = Product.objects.filter(store__id=pk)
    return render(request, 'store_product_list.html', {'store_product': store_product})


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
