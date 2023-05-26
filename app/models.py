from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
    
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    playlists = models.ManyToManyField(Playlist)

    def __str__(self) -> str:
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return self.name
    


