import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("MisssingValuesHandled.csv")

#Top Tracks
top_tracks = df['track_name'].value_counts().head(50)
print("Top 50 Most Played Tracks:")
print(top_tracks)

#Top Artists
top_artists = df['artist_name'].value_counts().head(50)
print("Top 50 Most Played Artists:")
print(top_artists)

#Top Albums
top_albums = df['album_name'].value_counts().head(10)
print("Top 10 Most Played Albums:")
print(top_albums)

# Total listening time in hours
total_ms = df['ms_played'].sum()
total_hours = total_ms / (1000 * 60 * 60)
print(f"Total Listening Time: {total_hours:.2f} hours")

listening_by_artist = df.groupby('artist_name')['ms_played'].sum().sort_values(ascending=False).head(10)
# Convert ms to hours
listening_by_artist = listening_by_artist / (1000 * 60 * 60)
print("Top 10 Artists by Listening Time (hours):")
print(listening_by_artist)


import os
os.makedirs("summaries", exist_ok=True)


top_tracks.to_csv("summaries/top_tracks.csv")
top_artists.to_csv("summaries/top_artists.csv")
top_albums.to_csv("summaries/top_albums.csv")
listening_by_artist.to_csv("summaries/listening_by_artist.csv")
