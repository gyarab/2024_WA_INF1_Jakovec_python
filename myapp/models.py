from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Band(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    band = models.ForeignKey('myapp.Band', on_delete=models.CASCADE, related_name='albums')
    cover_url = models.URLField(max_length=200, blank=True, null=True)  # URL to the album cover image

    def __str__(self):
        return f"{self.title} - {self.band.name}"

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey('myapp.Album', on_delete=models.CASCADE,  related_name='songs')
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.album.title}"

class Comment(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    song = models.ForeignKey('Song', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

    def __str__(self):
        return f"{self.username}: {self.text[:50]}"

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')