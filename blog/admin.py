from django.contrib import admin
from .models import User, Post, Origin, Category, Product, Store


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Origin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)

# Register your models here.
