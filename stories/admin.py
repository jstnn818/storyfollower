from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner')
    ordering = ('title', 'author', 'owner')
    search_fields = ('title', 'author', 'owner')