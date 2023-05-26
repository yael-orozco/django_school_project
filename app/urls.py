from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.noargs),
    path('albums/details/<int:id>', views.album_details, name='album_details'),
    path('add_album/', views.add_album, name='add_album'),
    path('delete_album/<int:id>', views.delete_album, name='delete_album'),
    path('add_song_to_album/<int:id>', views.add_song_to_album, name='add_song_to_album'),
    path('song_details/<int:id>', views.song_details, name='song_details'),
    path('delete_song/<int:id>', views.delete_song, name='delete_song'),
    path('artist_details/<int:id>', views.artist_details, name='artist_details'),
    path('update_artist/<int:id>', views.update_artist, name='update_artist'),
    path('new_playlist', views.create_playlist, name='new_playlist'),
    path('playlist_details/<int:id>', views.playlist_details, name='playlist_details'),
    path('add_song_to_playlist/<int:id>', views.add_song_to_playlist, name='add_song_to_playlist'),
    path('all_albums/', views.all_albums, name='all_albums'),
    path('delete_from_playlist/<int:playlist_id>/<int:song_id>', views.delete_from_playlist, name='delete_from_playlist')
]