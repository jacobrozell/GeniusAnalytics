from GeniusArtist import GeniusArtist
import GeniusAPI
import GeniusCSV
import GeniusUtil

# ---------- Scripting Util ----------
@GeniusUtil.timer_sec
def get_songs(artist_id):
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
    return songs

@GeniusUtil.timer_sec
def get_full_songs(artist, songs, filePath):
    cache_file = f'cache/{artist.id}_{artist.name}.pkl'
    cache_if_exists = GeniusUtil.get_cache(cache_file)
    errors = 0

    if cache_if_exists:
        print(f'Found {cache_file} cache!')
        full_songs = cache_if_exists
    else:
        print(f'{cache_file} full empty.')
        print("This will take some time....")

        full_songs = []
        for (index, song) in enumerate(songs):
            try:
                print(f'{index}/{len(songs)}')
                full_song = GeniusAPI.get_song_from_id(song['id'])
                if full_song:
                    full_songs.append(full_song)
            except:
                errors += 1
                continue

    GeniusUtil.cache(file=cache_file, data=full_songs)
    GeniusCSV.write_songs(full_songs, filePath)
    print(f'{filePath} created.\nErrors: {errors}')
    return songs 


def populate_artist(artist_name) -> GeniusArtist:
    # Look for artist name in cache before searching
    artist = GeniusAPI.search(artist_name)
    print(f'Artist_id found: {artist.id}\n')

    artist_cache_file = f'cache/artists/{artist.id}_{artist.name}.pkl'
    cache_if_exists = GeniusUtil.get_cache(artist_cache_file)

    if cache_if_exists:
        print('Cache found!')
        artist = cache_if_exists
    else:
        songs = get_songs(artist.id)
        full_songs = get_full_songs(
            artist=artist, 
            songs=songs, 
            filePath=f'songs/{artist.id}_{artist.name}_fullsongs.csv'
        )

        artist.songs = full_songs
        GeniusUtil.cache(file=f'cache/artists/{artist.id}_{artist.name}.pkl', data=artist)

    artist.make_csv()
    print(f'Done with {artist_name}.\n')
    return artist 

# ---------- Script ----------
print("---------- Genuis Analytics ----------")
artist_names = ["peach pit", "kings of leon"]
artists = []

for name in artist_names:
    artists.append(populate_artist(name))

for artist in artists:
    print(artist.name)


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
