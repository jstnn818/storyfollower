from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.story_list_all, name="story-list-all"),
    path('', views.home, name="home"),
]