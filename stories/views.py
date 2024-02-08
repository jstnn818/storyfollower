from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Story
from .forms import StoryForm

@login_required
def home(request):
    story_sort = request.GET.get('sort', 'title')
    story_list = Story.objects.filter(owner=request.user.id).order_by(story_sort)
    
    # Not updating correctly
    recent_sort = request.GET.get('sort', '-date_accessed')
    recent_list = Story.objects.filter(owner=request.user.id).order_by(recent_sort)
    
    return render(request, "stories/home.html", {
        'user': request.user,
        'recent_list': recent_list[:4],
        'story_list': story_list[:8],
        'story_list_length': len(story_list)
    })

@login_required
def story_list_all(request):
    sort = request.GET.get('sort', 'title')
    story_list = Story.objects.filter(owner=request.user.id).order_by(sort)
    return render(request, "stories/story_list.html", {
        'story_list': story_list,
    })

@login_required
def add_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
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
    if request.user == story.owner:
        form = StoryForm(request.POST or None, request.FILES or None, instance=story)
        if form.is_valid():
                form.save()
                return redirect('story-page', story_id=story.id)
        return render(request, "stories/update_story.html", {
            'story': story,
            'form': form,
        })
    else:
        return redirect('members:access-denied', owner_id=story.owner.id)
    
@login_required
def update_notes(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.user == story.owner:
        if request.method == 'POST':
            notes = request.POST.get('content')
            print(notes)
            story.notes = notes
            story.save()
        return render(request, "stories/story_page.html", {
            'story': story,
        })
    else:
        return redirect('members:access-denied', owner_id=story.owner.id)

@login_required
def download_notes(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.user == story.owner:
        response = HttpResponse(content_type="text/plain")
        response['Content-Disposition'] = f"attachment; filename={story.title} - Notes.txt"
        lines = [f"=={story.title}==\n\n{story.notes}"]
        response.writelines(lines)
        return response
    else:
        return redirect('members:access-denied', owner_id=story.owner.id)

@login_required
def delete_story(request, story_id):
    story = Story.objects.get(pk=story_id) 
    if request.user == story.owner:
        story.delete()
        return redirect('story-list-all')
    else:
        return redirect('members:access-denied', owner_id=story.owner.id)

@login_required
def story_page(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.user == story.owner:
        return render(request, "stories/story_page.html", {
            'story': story,
        })
    else:
        return redirect('members:access-denied', owner_id=story.owner.id)

@login_required
def search_stories(request):
    if request.method == "POST":
        searched = request.POST['searched']
        story_list = Story.objects.filter(owner=request.user.id).filter(title__contains=searched)
    return render(request, "stories/search_stories.html", {
        'searched': searched,
        'story_list': story_list,
    })