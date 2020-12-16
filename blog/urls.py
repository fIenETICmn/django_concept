from django.contrib import admin
from django.urls import path
# from .views import post_list, signup
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list/', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('signup/', views.signup, name='signup'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
]