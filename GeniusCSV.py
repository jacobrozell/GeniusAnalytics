import csv
import pandas as pd
from GeniusSong import GeniusFullSong

def write_songs(songs: GeniusFullSong, file):
    """
    Write songs to a csv.
    `songs`: [GeniusFullSong]
    """
    print(f'Writing to {str(file)}...')
    with open(file, 'w+') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(songs[0].make_header())

        for song in songs:
            csvwriter.writerow(song.make_row())

def get_column_from_csv(file, value):
    """
    Read column from csv.
    `file`: Name of CSV file to read from.
    `value`: column_name to read from the CSV.
    Returns -> List[Values]
    """
    df = pd.read_csv(file)
    try:
        values = df.value
    except:
        print(f'{file} didn\'t have {value}')
        return

    return values
