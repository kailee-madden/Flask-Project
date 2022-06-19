import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import random

client_credentials_manager = SpotifyClientCredentials(client_id="6c449b3966964f9e865d70a8709bf77f",
                                                      client_secret="d107d61ca36345a98c3ac72d523875f9")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


username="kailee.madden"
playlist_id="4kOz4MxGsxuWLmP4ZaSsOz"
songs = {}
results = sp.user_playlist(username, playlist_id, fields="tracks(items(track(id, name)))")
for element in results['tracks']['items']:
    songs.update({element['track']['name']:element['track']['id']})
random_songs = {k: songs[k] for k in random.sample(songs.keys(),2)}
print(random_songs)
print(len(results['tracks']['items']))