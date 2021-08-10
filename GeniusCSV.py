import csv

# Write songs to a csv
#
# `songs`: [GeniusSong]
def write_songs(songs, file):
    print(f'Writing to {str(file)}...')
    with open(file, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(songs[0].make_header())

        for song in songs:
            csvwriter.writerow(song.make_row())

    print(f'{file} created!')

# Read column from csv
#
# `file`: Name of CSV file to read from
# `value`: column_name to read from the CSV
#
# Returns -> List[Values]
#
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
