from ArtistStats import ArtistStats
import config
import GeniusCSV
from GeniusSong import GeniusSong, GeniusFullSong
import requests
from pprint import pprint


root_url = "https://api.genius.com/"
headersMap = {
            "User-Agent": "CompuServe Classic/1.22",
            "Accept": "application/json",
            "Authorization": "Bearer " + config.api_key
    }


def search(query):
    """
    Search documents hosted on Genius.

    `query`: str - Can be artist or song

    Returns instance of ArtistStats

    https://docs.genius.com/#search-h2
    """

    search_path = f'search'
    params = {"q": query}
    repsonse = requests.request(method="GET", url=root_url+search_path, params=params, headers=headersMap).json()

    try:
        repsonse = repsonse['response']['hits'][0]['result']
    except:
        repsonse = repsonse['meta']
        print(f'Search_API error: {repsonse}')
        return

    return ArtistStats(json=repsonse)


def get_all_songs(artist_id: int):
    """
    Gets all songs for an artist_id
    
    `artist_id`: int - genius artist id
    Returns -> List[GeniusSong]
    
    https://docs.genius.com/#artists-h2
    """
    song_path = f'artists/{str(artist_id)}/songs'
    page = 1
    songs = []
    while page is not None:
        params = {"page": page, "per_page": "50"}
        repsonse = requests.request(method="GET", url=root_url+song_path, params=params, headers=headersMap).json()

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

def get_song_from_id(song_id):
    """
    Gets a specific song from song id
    This returns a song that has much more information than the `get_all_songs` path.
    
    `song_id`: int - genius song id
    https://docs.genius.com/#songs-h2
    """
    response = requests.request(method="GET", url=f'https://api.genius.com/songs/{str(song_id)}', headers=headersMap).json()

    try:
        song = response['response']['song']
        return song
    except:
        error = response['error']
        print(error)
        return None

# ---------- API Util ----------
def get_all_full_songs(file):
    """
    Gets all full songs from the `get_song_from_id`.
    Returns array of full strings.
    `file`: str - file to grab id column from
    """
    full_songs = []
    for id in GeniusCSV.get_column_from_csv(f'{file}', 'id'):
        full_song = get_song_from_id(id)
        full_songs.append(GeniusFullSong(full_song))
    return full_songs
