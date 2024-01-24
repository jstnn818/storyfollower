from django.urls import path
from . import views

urlpatterns = [
    path('home', views.story_list_all, name="story-list-all"),
    path('add_story', views.add_story, name="add-story"),
    path('story_page/<story_id>', views.story_page, name="story-page"),
]