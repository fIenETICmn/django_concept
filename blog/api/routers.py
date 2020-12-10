from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.viewsets import UserViewSet, PostViewSet
from blog.api import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'users', viewsets.UserViewSet)
router.register(r'posts', viewsets.PostViewSet)

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', include(router.urls)),
])
urlpatterns += router.urls