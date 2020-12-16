from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth import settings


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=30, unique=False)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Post(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    ]
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/',default='')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=120)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.categoryname


class Product(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# only one object will be created for this model as save method is overrod
class Origin(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name