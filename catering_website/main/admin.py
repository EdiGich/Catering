from django.contrib import admin
from .models import MenuItem, GalleryItem, ContactMessage, Event, News

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

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('date', 'time')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)