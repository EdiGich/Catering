from django.contrib import admin
from .models import MenuItem, GalleryItem, ContactMessage

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'sent_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('sent_at',)