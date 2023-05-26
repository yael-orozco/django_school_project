from django.contrib import admin
from .models import Album, Song, Artist, Playlist

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']

admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'album']

admin.site.register(Song, SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(Artist, ArtistAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(Playlist, PlaylistAdmin)
