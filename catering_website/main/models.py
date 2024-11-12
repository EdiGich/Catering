from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)  # Add image field
    description = models.TextField(blank=True)  # New field
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)  

    
    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery_images/')
    
    def __str__(self):
        return self.title