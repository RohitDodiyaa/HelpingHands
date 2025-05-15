# Register your models here.
from django.contrib import admin
from .models import Cause, Event, News, Volunteer

class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'content', 'author')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message')

admin.site.register(Cause, CauseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Volunteer, VolunteerAdmin)