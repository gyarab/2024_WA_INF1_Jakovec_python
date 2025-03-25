from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    band = models.ForeignKey('myapp.Band', on_delete=models.CASCADE, related_name='albums')

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