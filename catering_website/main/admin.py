from django.contrib import admin
from .models import MenuItem, GalleryItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)