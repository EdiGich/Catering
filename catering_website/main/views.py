from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import MenuItem, GalleryItem
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import LoginSerializer, GalleryItemSerializer

# Regular views for your Django pages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def sample_menus(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'sample_menus.html', context)

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

            # Email composition
            email_subject = f"Message from {name}"
            email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            from_email = 'noreplydtcaterers@gmail.com'

            # Send the email
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

# DRF Views for API endpoints

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

class GalleryItemUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # saves the gallery item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function-based view for gallery item upload (Optional)
@api_view(['POST'])
def upload_gallery_item(request):
    if request.method == 'POST':
        serializer = GalleryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # saves the gallery item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
