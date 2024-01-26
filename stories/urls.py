from django.urls import path
from . import views

urlpatterns = [
    path('home', views.story_list_all, name="story-list-all"),
    path('add_story', views.add_story, name="add-story"),
    path('update_story/<story_id>', views.update_story, name="update-story"),
    path('story_page/<story_id>', views.story_page, name="story-page"),
    path('search_stories', views.search_stories, name="search-stories"),
]