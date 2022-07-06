from django import forms
from .models import Comment, Event


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date', 'location', 'content', 'excerpt')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Title'
                }),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'
                }),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Location',
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Description',
                'max-width': '200px', 'max-heigth': '200px'
                }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Excerpt',
                'max-width': '50px', 'max-heigth': '100px'
                }),
        }
