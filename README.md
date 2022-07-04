# Flask-Project

### Requirements
- Python3
- Flask must be installed
- Valid Spotify credentials to access the API through spotipy library

### Usage
- This app is hosted on Google Cloud and it is recommended to host on a similar platform so that accessibility is not limited to when your localhost is running. 
- Enter a valid song from the song list or enter a new playlist id to generate a new list of songs.
- Once you have selected a valid song, a list of suggested songs will be populated.

### Recommendation Algorithm
The recommendation algorithm used is based on proximity, specifically Euclidean distance. Song features are normalized, scaled, and compressed into two representative features using PCA. Then the distance is measured and the nearest songs are provided as the recommendations. This is a form of WHAT TYPE OF RECOMMENDATION ALGORITHM IT IS