import GeniusAPI
import GeniusCSV
import pandas as pd
from pprint import pprint
import Util


@Util.timer_sec
def create_artist_csv(file, artist_id):
    cache_file = f'{artist_id}.pkl'
    cache_if_exists = Util.get_cache(cache_file)
    if cache_if_exists:
        print(f'Found {cache_file} cache!')
        songs = cache_if_exists
    else:
        print(f'{cache_file} empty.')
        songs = GeniusAPI.get_all_songs(artist_id)

    Util.cache(file=cache_file, data=songs)
    GeniusCSV.write_songs(songs, file)


# ---------- Script ----------
artist_id = 820
artist_name = "mac_miller"

file = f'songs/{artist_id}_{artist_name}_songs.csv'

create_artist_csv(file, artist_id)

# Get full song information to extract album information
# full_songs = []
# for id in GeniusCSV.get_column_from_csv(f'songs/{file}', 'id'):
#     full_song = GeniusAPI.get_song_from_id(id)
#     full_songs.append(full_song)

# ----- Top Songs
print("Working")
df = pd.read_csv(file)
valid_table = df.loc[:, 'title':'views']
#valid_table = valid_table.replace(to_replace='None', value=np.nan).dropna()
valid_table = valid_table.sort_values('views', ascending=False)
print(valid_table.head(10))
valid_table.to_csv(f'top_songs/{artist_id}_{artist_name} top_songs.csv', index=False)

# ----- Top Albums
# Genius's endpoint for albums is forbidden.
# I'll have to grab albums from full-songs json.

# ----- Top Words Per Song

# ----- Send to GoogleDrive

# ---- TODO / Brainstorm ----
# CLI wrapper
# Pull from Google Drive to Tabluea
# Lyric Analysis with frequency analysis

# Another API for album sales? 
##  Need new API for albums
# Top words used in top albums by sale
