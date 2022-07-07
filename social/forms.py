from django import forms
from .models import Comment, Event
from .widgets import DateTimePickerInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment here'
            })
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Title'
                }),
            'date': DateTimePickerInput(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Location',
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add all necessary information here',
                'max-width': '200px', 'max-heigth': '200px'
                }),
        }
