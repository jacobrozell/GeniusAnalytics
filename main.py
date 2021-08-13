import GeniusAPI
import GeniusCSV
import GeniusUtil
import pandas as pd
import numpy as np
import ArtistStats

# ---------- Scripting Util ----------
@GeniusUtil.timer_sec
def create_artist_csv(file, artist_id):
    cache_file = f'cache/{artist_id}.pkl'
    cache_if_exists = GeniusUtil.get_cache(cache_file)
    if cache_if_exists:
        print(f'Found {cache_file} cache!')
        songs = cache_if_exists
    else:
        print(f'{cache_file} empty.')
        print("This may take some time....")
        songs = GeniusAPI.get_all_songs(artist_id)

    GeniusUtil.cache(file=cache_file, data=songs)
    GeniusCSV.write_songs(songs, file)
    return songs

@GeniusUtil.timer_sec
def create_artist_csv_full_song(readFile, file, artist_id):
    cache_file = f'cache/{artist_id}_full.pkl'
    cache_if_exists = GeniusUtil.get_cache(cache_file)
    if cache_if_exists:
        print(f'Found {cache_file} cache!')
        songs = cache_if_exists
    else:
        print(f'{cache_file} full empty.')
        print("This may take some time....")
        songs = GeniusAPI.get_all_full_songs(readFile)

    GeniusUtil.cache(file=cache_file, data=songs)
    GeniusCSV.write_songs(songs, file)
    return songs

# ---------- Script ----------
print("---------- Genuis Analytics ----------")
artist_name = "mac miller"
artist = GeniusAPI.search(artist_name)

print(f'Artist_id found: {artist.id}\n')

file = f'songs/{artist.id}_{artist.name}_songs.csv'
full_file = f'songs/{artist.id}_{artist.name}_fullsongs.csv'

create_artist_csv(file, artist.id)
full_songs = create_artist_csv_full_song(readFile=file, file=full_file, artist_id=artist.id)
artist.songs = full_songs
print(artist.songs)

# # ---------- Top Songs ----------
# df = pd.read_csv(full_file)
# valid_table = df.replace(to_replace='None', value=np.nan).dropna()
# valid_table = valid_table.sort_values('views', ascending=False)


# valid_table.to_csv(f'top_songs/{artist_id}_{artist_name} top_songs.csv', index=False)

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
