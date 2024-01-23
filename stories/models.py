from django.db import models

# Maybe Characters should go here

class Story(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    # Map, Characters(?), Cover Image
    
    def __str__(self):
        return self.title