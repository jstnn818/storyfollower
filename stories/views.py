from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Story
from .forms import StoryForm

def home(request):
    return render(request, "stories/home.html", {})

def story_list_all(request):
    story_list = Story.objects.all()
    return render(request, "stories/story_list.html", {
        'story_list': story_list,
    })
    
def add_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_story?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "stories/add_story.html", {
        'form': form,
        'submitted': submitted,
    })

def story_page(request, story_id):
    story = Story.objects.get(pk=story_id)
    return render(request, "stories/story_page.html", {
        'story': story,
    })