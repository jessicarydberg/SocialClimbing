from django import forms
from .models import Comment, Event
from django_summernote.admin import SummernoteModelAdmin


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm, SummernoteModelAdmin):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location', 'content', 'image')
        summernote_fields = ('content')
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title'
                }),
            'date': forms.TextInput(attrs={
                'placeholder': 'Date'
                }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Location'
                }),
            'content': forms.TextInput(attrs={
                'placeholder': 'Description'
                }),
            'image': forms.TextInput(attrs={
                'placeholder': 'Image'
                }),
        }
