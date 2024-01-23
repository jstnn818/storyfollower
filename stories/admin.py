from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    ordering = ('title', 'author')
    search_fields = ('title', 'author')