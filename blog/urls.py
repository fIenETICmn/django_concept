from django.contrib import admin
from django.urls import path
from .views import post_list
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup', views.signup, name='signup'),
]