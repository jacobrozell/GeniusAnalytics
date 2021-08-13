import csv
import pandas as pd

def write_songs(songs, file):
    """
    Write songs to a csv.
    `songs`: [GeniusSong]
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
