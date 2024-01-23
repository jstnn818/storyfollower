from django import forms
from django.forms import ModelForm
from .models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'author', 'description')
        
        labels = {
            'title': '',
            'author': '',
            'description': '',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }