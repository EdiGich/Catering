from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views
# from .views import CustomTokenObtainPairView, upload_gallery_item, GalleryItemManageView, MenuItemViewSet, contact, get_messages
from .views import CustomTokenObtainPairView, upload_gallery_item, GalleryItemManageView, MenuItemViewSet, ContactMessagesViewSet, NewsViewSet, EventsViewSet
router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
# The `menu` API endpoint is automatically handled by DefaultRouter for MenuItemViewSet.
# This includes CRUD operations like list, create, update, delete.

router.register(r'messages', ContactMessagesViewSet)
router.register(r'news', NewsViewSet)
router.register(r'events', EventsViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),                                                                                             
    
    path('services/', views.services, name='services'),
    path('sample_menus/', views.sample_menus, name='sample_menus'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news_events, name='news'),
    path('contact/', views.contact, name='contact'),
    # path('api/get-messages/', views.get_messages, name='get_messages'),
    path('terms/', views.terms, name='terms'),

    path('api/', include(router.urls)),

    # JWT Token endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Gallery API endpoints
    path('api/galleryitem/upload/', upload_gallery_item, name='upload_gallery_item'),  # Upload endpoint
    path('api/galleryitem/manage/', GalleryItemManageView.as_view(), name='galleryitem-manage'),
    path('api/galleryitem/manage/<int:pk>/', GalleryItemManageView.as_view(), name='galleryitem-manage-detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
