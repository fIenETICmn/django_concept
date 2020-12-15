from django.contrib import admin
from django.urls import path, include
from blog.api.routers import router
from rest_framework_simplejwt import views as jwt_views
# from django.conf.urls.static import static
# from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
]
