from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )