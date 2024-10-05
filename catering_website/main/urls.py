from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Import JWT views from package
from .views import CustomTokenObtainPairView  # Import your custom view if it exists

# from .views import home, about, services, sample_menus, gallery, contact, terms


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('sample_menus/', views.sample_menus, name='sample_menus'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom JWT view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token view

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)