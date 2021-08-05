import json
from GeniusSong import GeniusSong
import config
import csv
from dateutil.parser import parse
import pandas as pd
from pprint import pprint
import requests

# https://api.genius.com/search?q=hello&access_token=[your-access-token]

root_url = "https://api.genius.com/"

# ----- API Functions -----

# Gets all songs for an artist_id
#
# `artist_id`: int - genius artist id
# Returns -> List[GeniusSong]
#
# https://docs.genius.com/#artists-h2
def get_all_songs(artist_id: int):
    song_path = f'artists/{str(artist_id)}/songs'

    page = 1
    songs = []
    while page is not None:
        params = {"page": page, "per_page": "50", 'access_token': config.api_key}
        repsonse = requests.request(method="GET", url=root_url+song_path, params=params).json()

        try:
            repsonse = repsonse['response']
            page = repsonse['next_page']
        except:
            error = repsonse['error']
            print(error)
            return []

        for song in repsonse['songs']:
            songs.append(GeniusSong(json=song))

    return songs


# Gets a specific song from song id
#
# `song_id`: int - genius song id
# https://docs.genius.com/#songs-h2
def get_song_from_id(song_id):
    params = {'access_token': config.api_key}
    response = requests.request(method="GET", url=f'https://api.genius.com/songs/{str(song_id)}', params=params).json()

    try:
        song = response['response']['song']['album']
        return song
    except:
        error = response['error']
        print(error)
        return None



# ----- CSV Write/Read -----

# Write songs to a csv
#
# `songs`: [GeniusSong]
def write_songs(songs, file):
    with open(file, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(songs[0].make_header())

        for song in songs:
            csvwriter.writerow(song.make_row())

    print(f'Done!\nFile: {csvfile}')


def get_column_from_csv(file, value):
    with open(file, 'r') as csvfile: 
        reader = csv.DictReader(csvfile)

        firstLine = True
        values = []
        for row in reader:
            if firstLine:
                firstLine = False
                continue

            values.append(row[value])

    return values



# Script
# ----- Get Songs
file = "mac_miller_songs.csv"
mac_id = 820
songs = get_all_songs(artist_id=mac_id)
write_songs(songs, file)
# ---------------------------------------------------

# ----- Get full song JSON from id
# ids = get_column_from_csv(file, 'id')

# full_songs = []
# for id in ids:  
#     full_songs.append(get_song_from_id(id))

# for song in full_songs:
#     print(song["release_date"])
# ---------------------------------------------------

# ----- Top Songs
def get_top_songs(file):
    df = pd.read_csv(file)
    print(df.head())
    titles = df.loc[:, "title"]
    views = df.loc[:, 'views']

    
get_top_songs(file)
# ---------------------------------------------------

# ----- Top Albums

# ----- Top Words Per Song

# ----- Send to GoogleDrive

# ----- Create Objects

# ---- TODO / Brainstorm ----
# CLI wrapper
# Pull from Google Drive to Tabluea
# Lyric Analysis with frequency analysis
# Another API for album sales? 
# Top words used in top albums by sale