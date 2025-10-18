import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("MisssingValuesHandled.csv")

#summaries
top_tracks = pd.read_csv("summaries/top_tracks.csv", index_col=0).squeeze("columns")
top_artists = pd.read_csv("summaries/top_artists.csv", index_col=0).squeeze("columns")
top_albums = pd.read_csv("summaries/top_albums.csv", index_col=0).squeeze("columns")
listening_by_artist = pd.read_csv("summaries/listening_by_artist.csv", index_col=0).squeeze("columns")

# Prepare top lists
top_tracks = df['track_name'].value_counts().head(50)
top_artists = df['artist_name'].value_counts().head(50)
top_albums = df['album_name'].value_counts().head(10)

# Listening time by artist
listening_by_artist = df.groupby('artist_name')['ms_played'].sum().sort_values(ascending=False).head(10)
listening_by_artist = listening_by_artist / (1000 * 60 * 60)  # convert to hours

# ====== PLOTTING STARTS ======

# Make plots look nicer
sns.set(style="whitegrid")

# Barplot for top 20 tracks
plt.figure(figsize=(12, 8))
top_tracks.head(20).sort_values().plot(kind='barh', color='skyblue')
plt.title("Top 20 Most Played Tracks")
plt.xlabel("Play Count")
plt.ylabel("Track Name")
plt.tight_layout()
plt.show()

#Top Artists
plt.figure(figsize=(12, 8))
top_artists.head(20).sort_values().plot(kind='barh', color='salmon')
plt.title("Top 20 Most Played Artists")
plt.xlabel("Play Count")
plt.ylabel("Artist Name")
plt.tight_layout()
plt.show()


#Top Albums
plt.figure(figsize=(10, 6))
top_albums.sort_values().plot(kind='barh', color='lightgreen')
plt.title("Top 10 Albums by Play Count")
plt.xlabel("Play Count")
plt.ylabel("Album Name")
plt.tight_layout()
plt.show()

# Top Albums
plt.figure(figsize=(10, 6))
ax = top_albums.sort_values().plot(kind='barh', color='lightgreen')

plt.title("Top 10 Albums by Play Count")
plt.xlabel("Play Count")
plt.ylabel("Album Name")

# Add value labels to the bars
for i, v in enumerate(top_albums.sort_values()):
    ax.text(v + 2, i, str(v), va='center')

plt.tight_layout()
plt.show()



#By Listening Time
plt.figure(figsize=(10, 6))
listening_by_artist.sort_values().plot(kind='barh', color='mediumpurple')
plt.title("Top 10 Artists by Listening Time (Hours)")
plt.xlabel("Listening Time (hours)")
plt.ylabel("Artist Name")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 8))
listening_by_artist.head(5).plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Top 5 Artists by Listening Time")
plt.ylabel("")
plt.tight_layout()
plt.show()




