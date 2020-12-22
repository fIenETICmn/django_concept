from blog.models import User, Post, Category, Store, Product, Productimage
from blog.api.serializers import UserSerializer, PostSerializer, CategorySerializer, \
    StoreSerializer, ProductSerializer, ProductimageSerializer
from rest_framework import viewsets
# from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductimageViewSet(viewsets.ModelViewSet):
    queryset = Productimage.objects.all()
    serializer_class = ProductimageSerializer
