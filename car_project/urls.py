
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("app.urls")),
    path("api-auth/", include("rest_framework.urls", namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
]