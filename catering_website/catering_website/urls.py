from django.contrib import admin
from django.urls import path, include
from main.views import handler404
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

handler404 = 'main.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Using your custom token view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('main.urls')),  # Includes the URLs from the main app
]
