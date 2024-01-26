from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Story
from .forms import StoryForm

def home(request):
    return render(request, "stories/home.html", {})

def story_list_all(request):
    story_list = Story.objects.all()
    return render(request, "stories/story_list.html", {
        'story_list': story_list,
    })

@login_required
def add_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.owner = request.user
            story.save()
            return HttpResponseRedirect('add_story?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "stories/add_story.html", {
        'form': form,
        'submitted': submitted,
    })

@login_required
def update_story(request, story_id):
    story = Story.objects.get(pk=story_id)
    form = StoryForm(request.POST or None, instance=story)
    if form.is_valid():
            form.save()
            return redirect('story-page', story_id=story.id)
    return render(request, "stories/update_story.html", {
        'story': story,
        'form': form,
    })

def story_page(request, story_id):
    story = Story.objects.get(pk=story_id)
    return render(request, "stories/story_page.html", {
        'story': story,
    })
    
def search_stories(request):
    if request.method == "POST":
        searched = request.POST['searched']
        story_list = Story.objects.filter(title__contains=searched)
    return render(request, "stories/search_stories.html", {
        'searched': searched,
        'story_list': story_list,
    })