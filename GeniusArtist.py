from pprint import pprint
from numpy import uint
from pandas import DataFrame


class GeniusArtist:
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
        rows = []
        for song in self.songs:
            rows.append(song.make_series())
        df = DataFrame({rows})
        pprint(df)
        return df

    def get_artist_dataframe(self):
         return DataFrame([{
            'id': self.id,
            'name': self.name,
            'iq': self.iq,
            'is_verified': self.is_verified,
            'image_url': self.image_url,
            'url': self.url, 
            #'top_song': self.get_top_songs_dataframe().sort_values('views', ascending=False).head(1)
        }])

    def make_csv(self):
        self.get_artist_dataframe().to_csv(f'artists/{self.id}_{self.name}.csv')

