from typing import Optional

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
