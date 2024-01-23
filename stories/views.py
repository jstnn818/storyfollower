from django.shortcuts import render
from .models import Story

def home(request):
    return render(request, "stories/home.html", {})

def story_list_all(request):
    story_list = Story.objects.all()
    return render(request, "stories/story_list.html", {
        'story_list': story_list,
    })
