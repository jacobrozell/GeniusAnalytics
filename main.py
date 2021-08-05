import requests
from pprint import pprint
import matplotlib as plt
import csv
from dateutil.parser import parse
from requests import api
import config
from requests.api import head

# https://api.genius.com/search?q=hello&access_token=[your-access-token]

root_url = "https://api.genius.com/"

print(config.api_key)

def get_songs():
    song_path = "artists/820/songs"
    page = 1
    songs = []
    while page is not None:
        params = {"page": page, "per_page": "50", 'access_token': config.api_key}
        repsonse = requests.request(method="GET", url=root_url+song_path, params=params).json()
        print(repsonse)
        repsonse = repsonse['response']
        page = repsonse['next_page']
        for song in repsonse['songs']:
            songs.append(song)
    return songs

def write_songs(songs):
    with open("mac_miller_songs.csv", 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(["Count", "Title", "Id", "PageViews", "URL", "Song_Art_URL"])

        count = -1
        for song in songs:
            count += 1
            try:
                pageviews = song['stats']['pageviews']
            except:
                pageviews = None

            row = [
                str(count), 
                str(song['title_with_featured']), 
                str(song['id']), 
                pageviews, 
                str(song['url']), 
                str(song['song_art_image_url'])
            ]
            csvwriter.writerow(row)
    print("Done!")

def get_song_ids():
    with open("mac_miller_songs.csv", 'r') as csvfile: 
        reader = csv.DictReader(csvfile)

        firstLine = True
        ids = []
        for row in reader:
            if firstLine:
                firstLine = False
                continue

            ids.append(row["Id"])

    return ids

def get_song_from_id(id):
    params = {'access_token': api_key}
    response = requests.request(method="GET", url=f'https://api.genius.com/songs/{str(id)}', params=params).json()
    return response['response']['song']['album']

songs = get_songs()
write_songs(songs)

# ids = get_song_ids()
# full_songs = []
# for id in ids:  
#     full_songs.append(get_song_from_id(id))

# for song in full_songs:
#     print(song["release_date"])

# ---- TODO ----
# Song by popularity
# Top Albums
# Ability to generate worksheet from artist id / CLI
# Google drive API
# Object-oriented
# Tabluea
# Machine learning / lyric analysis
# Top words by album
# PUSH TO GIT