# Flask-Project

### Requirements
- Python3
- Flask must be installed
- Valid Spotify credentials to access the API through spotipy library to update the songs available

### Usage
- This REST API is hosted through Flask
- Enter a valid song from the song list and five suggested songs will be return in json format
- Or use the get_user_track_data.py functions to enter a new playlist id to generate a new list of songs

### Recommendation Algorithm
The recommendation algorithm used is based on proximity, specifically Euclidean distance. Song features are normalized, scaled, and compressed into two representative features using PCA. Then the distance is measured and the nearest songs are provided as the recommendations. This is a form of WHAT TYPE OF RECOMMENDATION ALGORITHM IT IS
