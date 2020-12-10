from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='enter valid email')

    class Meta:
        model = User
        fields = ('username',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )