from rest_framework import serializers
from blog.models import User, Post, Category, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'id', 'url',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'id', 'url',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryname',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ('category', 'id', 'url',)