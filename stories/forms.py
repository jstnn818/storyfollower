from django import forms
from django.forms import ModelForm
from .models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'author', 'description', 'cover', 'banner')
        
        labels = {
            'title': '',
            'author': '',
            'description': '',
            'cover': '',
            'banner': '',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }