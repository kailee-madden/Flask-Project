#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
import math

def normalize(dataframe):
    name = dataframe['name']
    dataframe.drop(['energy','loudness', 'uri', 'name'], axis=1, inplace=True)
    #normalize using min max scaling aka subtract min value of feature than divide by range to get range of [0,1]
    x = dataframe.values 
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df=pd.DataFrame(x_scaled, columns=dataframe.columns)

    #get principal components
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x_scaled)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

    #normalize again
    x = principalDf.values 
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df=pd.DataFrame(x_scaled, columns=principalDf.columns)
    
    df['Name'] = name # add song name back in
    return df

def generate_playlist_recs(df, song): 
    # checks the euclidean distance between the song and all others, selects top 5 closest
    playlist = []
    song_row = df.loc[df['Name'] == song]
    pc1 = song_row['principal component 1']
    pc2 = song_row['principal component 2']

    for index, row in df.iterrows():
        if row['Name'] == song:
            continue
        else:
            distance = math.dist([pc1, pc2], [row['principal component 1'], row['principal component 2']])
            playlist.append((row['Name'], distance))
    playlist.sort(key = lambda x: x[1])

    final_playlist = [n for (n, d) in playlist[0:5]]

    return final_playlist

def recommend(title):
    music_df = pd.read_csv("kailee.madden-4kOz4MxGsxuWLmP4ZaSsOz.csv")

    normalized_df = normalize(music_df)
    playlist_recs = generate_playlist_recs(normalized_df, title)

    return playlist_recs