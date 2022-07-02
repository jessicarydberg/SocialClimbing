from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_filter = ('status', 'date', 'location')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'date', 'location')
    search_fields = ('date', 'location', 'title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'event')
    list_display = ('created_on', 'event', 'body', 'name', 'approved')
    search_fields = ('approved', 'event', 'name',)
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)