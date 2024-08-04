from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import MenuItem, GalleryItem

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def sample_menus(request):
    menu_items = MenuItem.objects.all()
    context = { 'menu_items': menu_items}
    return render(request, 'sample_menus.html', context)

def gallery(request):
    gallery_items = GalleryItem.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            # Send email (for example purposes, adjust settings as necessary)
            send_mail(
                f"Message from {name}",
                message,
                email,
                ['youremail@example.com'], # Replace with your email
                fail_silently=False,
            )
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form=ContactForm()
    return render(request, 'contact.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')