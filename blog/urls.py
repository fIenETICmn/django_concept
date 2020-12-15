from django.contrib import admin
from django.urls import path
# from .views import post_list, signup
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
]