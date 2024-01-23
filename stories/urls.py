from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.story_list_all, name="story-list-all"),
    path('stories/add_story', views.add_story, name="add-story"),
    path('', views.home, name="home"),
]