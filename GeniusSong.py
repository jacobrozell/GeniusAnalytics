from typing import Optional
from pandas import DataFrame, Series

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
    album_json = None
    media_json = None
    album_name: str = None
    album_id: str = None
    album_url: str = None
    spotify_link: str = None
    
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
            self.album_name = None
            self.album_id = None
            self.album_url = None

        try:
            self.media_json = json['media']
            for object in self.media_json:
                if object['provider'] == 'spotify':
                    self.spotify_link = object['url']
        except:
            self.spotify_link = None

    def make_header(self):
        return [
            "id",
            "title",
            "views",
            "release_date",
            'user_interest',
            'album_name',
            'spotify_link',
            "lyric_url",
            "art_url",
        ]

    def make_row(self):
        return [
            self.id,
            self.title, 
            self.views,
            self.release_date,
            self.user_interest,
            self.album_name, 
            self.spotify_link,
            self.lyrics_url,
            self.art_url
        ]

    