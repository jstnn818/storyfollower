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
    date_accessed = models.DateTimeField(auto_now=True)

    @classmethod
    def from_db(cls, db, field_names, values):
        obj = super().from_db(db, field_names, values)
        obj.save()
        return obj
    
    def __str__(self):
        return self.title