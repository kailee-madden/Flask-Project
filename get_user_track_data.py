#!/usr/bin/env python3
import argparse
import sys
import os
import subprocess
import json
import spotipy
import spotipy.util as util
import pandas as pd
import random
from contextlib import suppress

from spotipy.oauth2 import SpotifyClientCredentials

#get the authorization necessary from the spotify api
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, 
                                                    client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username=USERNAME
playlist_id=ID

def get_playlist_songs(username, playlist_id, sp):
    songs = {}
    ids = []
    results = sp.user_playlist(username, playlist_id, fields="tracks(items(track(id, name)))")
    for element in results['tracks']['items']:
        songs.update({element['track']['name']:element['track']['id']})
    return songs

def get_audio_features(username, playlist_id, tracks={}):
    ids = []
    names = []
    for key, value in tracks.items():
        ids.append(value)
        names.append(key)
    audio_features = sp.audio_features(ids)
    features_list = []
    for features in audio_features:
        features_list.append([features['energy'], features['liveness'],
                              features['tempo'], features['speechiness'],
                              features['acousticness'], features['instrumentalness'],
                              features['time_signature'], features['danceability'],
                              features['key'], features['duration_ms'],
                              features['loudness'], features['valence'],
                              features['mode'],features['uri']])
    
    i = 0
    for name in names:
        features_list[i].append(name)
        i += 1
    
    df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                                'tempo', 'speechiness',
                                                'acousticness', 'instrumentalness',
                                                'time_signature', 'danceability',
                                                'key', 'duration_ms', 'loudness',
                                                'valence', 'mode',
                                                'uri', 'name'])
    df.to_csv('{}-{}.csv'.format(username, playlist_id), index=False)
    return features_list


def main(username, playlist_id):
    print("Getting your playlist songs...")
    song_dic = get_playlist_songs(username, playlist_id, sp)
    audio = get_audio_features(username, playlist_id, song_dic)
    return audio

if __name__ == '__main__':
    print("Starting...")
    main(username, playlist_id)
    print("A CSV file with the relevant audio feature data for your playlist has been generated.")
