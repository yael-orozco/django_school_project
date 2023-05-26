from django.shortcuts import render, redirect
from .forms import CreateUserForm, AddAlbumForm, AddSongToAlbumForm, UpdateArtistForm, CreatePlaylistForm, AddSongToPlaylistForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Album, Song, Artist, Playlist
from django.contrib.auth.models import User
import os

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                artist = Artist(name=user.username, description='', user=user)
                artist.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)

                return redirect('login')

        return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
                return render(request, 'login.html', {})

        return render(request, 'login.html', {})

@login_required(login_url='login')
def home(request):
    albums = Album.objects.filter(author=request.user)
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'home.html', {'albums': albums, 'playlists': playlists})

def logout_user(request):
    logout(request)
    return redirect('login')

def noargs(request):
    return redirect('login')

@login_required(login_url='login')
def album_details(request, id):
    album = Album.objects.get(id=id)
    songs = Song.objects.filter(album=album)
    return render(request, 'album_details.html', {'album': album, 'songs':songs})

def delete_album(request, id):
    album = Album.objects.get(id=id)
    os.remove('.' + album.image.url)
    album.delete()
    return redirect('home')

def song_details(request, id):
    song = Song.objects.get(id=id)
    return render(request, 'song_details.html', {'song': song})

def delete_song(request, id):
    song = Song.objects.get(id=id)
    album_id = song.album.id
    song.delete()
    return redirect('album_details', id=album_id)

def artist_details(request, id):
    artist = Artist.objects.get(user_id=id)
    albums = Album.objects.filter(author=artist.user)
    return render(request, 'artist_details.html', {'artist': artist, 'albums':albums})

def update_artist(request, id):
    artist = Artist.objects.get(user_id=id)
    form = UpdateArtistForm(request.POST or None, instance=artist)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'update_artist.html', {'form':form, 'artist': artist})

def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            album.author = request.user
            album.save()
            return redirect('home')
        
    form = AddAlbumForm()
    return render(request, 'add_album.html', {'form': form})

def create_playlist(request):
    if request.method == 'POST':
        form = CreatePlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save()
            playlist.user = request.user
            playlist.save()
            return redirect('home')
        
    form = CreatePlaylistForm()
    return render(request, 'new_playlist.html', {'form': form})

def playlist_details(request, id):
    playlist = Playlist.objects.get(id=id)
    songs = Song.objects.filter(playlists=playlist)
    return render(request, 'playlist_details.html', {'playlist': playlist, 'songs': songs})

def add_song_to_album(request, id):
    album = Album.objects.get(id=id)
    form = AddSongToAlbumForm()
    if request.method == 'POST':
        form = AddSongToAlbumForm(request.POST)
        if form.is_valid():
            song = form.save()
            song.album = album
            song.save()
            return redirect('album_details', id=id)
    return render(request, 'add_song_to_album.html', {'album': album, 'form': form})

def add_song_to_playlist(request, id):
    song = Song.objects.get(id=id)
    form = AddSongToPlaylistForm()
    form.fields['playlist'].queryset = Playlist.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AddSongToPlaylistForm(request.POST)
        if form.is_valid():
            print('valid')
            playlist = form.cleaned_data['playlist']
            song.playlists.add(playlist)
            return redirect('home')
    return render(request, 'add_song_to_playlist.html', {'song': song, 'form': form})

def all_albums(request):
    albums = Album.objects.all()
    return render(request, 'all_albums.html', {'albums': albums})

def delete_from_playlist(request, playlist_id, song_id):
    song = Song.objects.get(id=song_id)
    playlist = Playlist.objects.get(id=playlist_id)
    song.playlists.remove(playlist)
    return redirect('playlist_details', id=playlist_id)