from typing import Optional
from pandas import DataFrame, Series

class GeniusSong:
    # Properties
    json = ""
    id: int
    title: str
    views: Optional[int]
    lyrics_url: str
    art_url: str

    # Init
    def __init__(self, json):
        self.json = json
        self.id = json['id']
        self.title = json['title_with_featured']
        self.lyrics_url = json['url']
        self.art_url = json['song_art_image_url']

        try:
            self.views = json['stats']['pageviews']
        except:
            self.views = None

    def make_header(self):
        return ["id", "title", "views", "lyric_url", "art_url"]

    def make_row(self):
        row = [
            str(self.id),
            str(self.title),
            self.views, 
            str(self.lyrics_url), 
            str(self.art_url)
        ]

        return row

class GeniusFullSong:
    # Properties
    json = ""
    id: int
    title: str
    views: Optional[int]
    lyrics_url: str
    art_url: str
    release_date: str  # yyyy-mm-dd
    release_date_for_display: str
    user_interest: int
    album_json = {}
    media_json = {}
    album_name: str
    album_id: str
    album_url: str
    spotify_link: str
    
    # Init
    def __init__(self, json):
        self.json = json
        self.id = json['id']
        self.title = json['title_with_featured']
        self.lyrics_url = json['url']
        self.art_url = json['song_art_image_url']

        try:
            self.views = json['stats']['pageviews']
        except:
            self.views = None

        self.release_date = json['release_date']
        self.release_date_for_display = json['release_date_for_display']
        self.user_interest = json['pyongs_count']

        try:
            self.album_json = json['album']
            self.album_name = self.album_json['name']
            self.album_id = self.album_json['api_path'].replace("/albums/", "")
            self.album_url = self.album_json['url']
        except:
            print("Error populating album properties.")

        try:
            self.media_json = json['media']
            for object in self.media_json:
                if object['provider'] == 'spotify':
                    self.spotify_link = object['url']
        except:
            print("Error populating media properties.")

    def make_series(self):
        return Series({
            "id": self.id,
            "title": self.title, 
            "views": self.views,
            "release_date": self.release_date,
            'user_interest': self.user_interest,
            'album_name': self.album_name, 
            'spotify_link': self.spotify_link,
            "lyric_url": self.lyrics_url,
            "art_url": self.art_url
        })

    def to_csv(self, file):
        self.make_series().to_csv(file)

    