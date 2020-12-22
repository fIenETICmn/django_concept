from django import forms
from .models import User, Post, Product, Category, Store, Productimage
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
        fields = ('title', 'text',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryname',)


class ProductimageForm(forms.ModelForm):
    class Meta:
        model = Productimage
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category',)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('__all__')