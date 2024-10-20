from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import ContactForm
from .models import MenuItem, GalleryItem
from .serializers import LoginSerializer, GalleryItemSerializer

# Standard Django Views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def sample_menus(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'sample_menus.html', {'menu_items': menu_items})

def gallery(request):
    gallery_items = GalleryItem.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Compose email
            email_subject = f"Message from {name}"
            email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            from_email = 'noreplydtcaterers@gmail.com'

            # Send email
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=from_email,
                to=['dtcdelicioustumainicaterers@gmail.com'],
                reply_to=[email]
            )
            email_message.send()

            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')

# Check if user is an admin
def is_admin(user):
    return user.is_superuser

# API Views using Django Rest Framework

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class GalleryItemManageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        gallery_items = GalleryItem.objects.all()
        serializer = GalleryItemSerializer(gallery_items, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            gallery_item = GalleryItem.objects.get(pk=pk)
            gallery_item.delete()
            return Response(status=204)
        except GalleryItem.DoesNotExist:
            return Response({'error': 'Gallery item not found'}, status=404)

    def put(self, request, pk, format=None):
        try:
            gallery_item = GalleryItem.objects.get(pk=pk)
            serializer = GalleryItemSerializer(gallery_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except GalleryItem.DoesNotExist:
            return Response({'error': 'Gallery item not found'}, status=404)

# DRF Class-based views for list, retrieve, update, and delete
class GalleryItemListView(generics.ListAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    permission_classes = [IsAuthenticated]

class GalleryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    permission_classes = [IsAuthenticated]

@method_decorator(csrf_exempt, name='dispatch')
class GalleryItemUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the gallery item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function-based API views for managing gallery items (alternative to class-based)
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_gallery_item(request):
    if request.method == 'POST':
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the gallery item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_gallery_item(request, item_id=None):
    """
    GET: List all gallery items or retrieve a specific one
    PUT: Edit a specific gallery item (title, description)
    DELETE: Delete a specific gallery item
    """
    try:
        if request.method == 'GET':
            if item_id:
                gallery_item = GalleryItem.objects.get(id=item_id)
                serializer = GalleryItemSerializer(gallery_item)
                return Response(serializer.data)
            else:
                gallery_items = GalleryItem.objects.all()
                serializer = GalleryItemSerializer(gallery_items, many=True)
                return Response(serializer.data)

        elif request.method == 'PUT':
            gallery_item = GalleryItem.objects.get(id=item_id)
            serializer = GalleryItemSerializer(gallery_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            gallery_item = GalleryItem.objects.get(id=item_id)
            gallery_item.delete()
            return Response({'message': 'Gallery item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except GalleryItem.DoesNotExist:
        return Response({'error': 'Gallery item not found'}, status=status.HTTP_404_NOT_FOUND)
