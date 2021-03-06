from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_filter = ('status', 'date', 'location')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'date', 'location')
    search_fields = ('date', 'location', 'title')
