from django.db import models
from django.contrib.auth.models import User

# Maybe Characters should go here

class Story(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to="images/")
    banner = models.ImageField(null=True, blank=True, upload_to="images/")
    # Map, Characters(?)
    
    def __str__(self):
        return self.title