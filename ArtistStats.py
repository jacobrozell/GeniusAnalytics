from pprint import pprint
from numpy import uint
from pandas import DataFrame


class ArtistStats:
    api_path: str
    header_image_url: str
    image_url: str
    iq: uint
    is_verified: bool
    url: str
    id: int
    name: str

    songs = {}

    def __init__(self, json):
        json = json['primary_artist']
        self.id = json['id']
        self.name = json['name']
        self.api_path = json['api_path']
        self.header_image_url = json['header_image_url']
        self.image_url = json['image_url']
        self.iq = json['iq']
        self.is_verified = json['is_verified']
        self.url = json['url']

    def get_top_songs_dataframe(self):
        return DataFrame({self.songs})
