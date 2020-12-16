from django.contrib import admin
from .models import User, Post, Origin, Category, Product


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Origin)
admin.site.register(Category)
admin.site.register(Product)

# Register your models here.
