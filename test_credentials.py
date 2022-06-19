import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import random

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, 
                                                    client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username=USERNAME
playlist_id=ID
songs = {}
results = sp.user_playlist(username, playlist_id, fields="tracks(items(track(id, name)))")
for element in results['tracks']['items']:
    songs.update({element['track']['name']:element['track']['id']})
random_songs = {k: songs[k] for k in random.sample(songs.keys(),2)}
print(random_songs)
print(len(results['tracks']['items']))
