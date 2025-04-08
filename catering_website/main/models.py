from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)  
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    
    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=MenuItem)
def delete_image_file(sender, instance, **kwargs):
    # Delete the image file from the filesystem when the MenuItem is deleted
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

class GalleryItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery_images/')
    
    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=13, blank=True)
    message = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='0')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def detail_url(self):
        return f"/events/{self.id}"  # Adjust based on your URL patterns


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def detail_url(self):
        return f"/news/{self.id}"  # Adjust based on your URL patterns