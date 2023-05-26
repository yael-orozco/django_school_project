from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Album, Artist, Song, Playlist

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'genre', 'image']

class AddSongToAlbumForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'link']

class UpdateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description']

class CreatePlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']

class AddSongToPlaylistForm(forms.Form):
    playlist = forms.ModelChoiceField(queryset=Playlist.objects.all())

